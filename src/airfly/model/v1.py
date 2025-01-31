import inspect
import os
from collections import deque
from functools import lru_cache
from types import FunctionType, MethodType, ModuleType
from typing import (
    Any,
    Dict,
    Generator,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)

import asttrs
import attr
import loguru
import networkx as nx
import regex as re

import airfly
from airfly._vendor import collect_airflow_operators
from airfly.utils import (
    blacking,
    collect_objects,
    immutable,
    isorting,
    issubclass_by_qualname,
    qualname,
)

TaskClass = Type["Task"]


BUILTIN_OPERATORS = collect_airflow_operators()


class Literal:

    def __init__(self, expr: str, deps: List[Any] = None):
        self.expr = expr
        self.deps = deps if isinstance(deps, List) else [deps]

    def __repr__(self):
        return self.expr

    def _to_ast(self):
        return asttrs.Name(id=self.expr, ctx=asttrs.Load())

    def _dep_ast(self, param_ctx: "ParamContext" = None) -> List[asttrs.stmt]:
        body = []

        for d in self.deps:

            if isinstance(d, Literal):
                body.append(d._to_ast())  # NOTE: alias conflict may occur
            else:
                body.extend(ParamContext.get(d, param_ctx)._dep_ast(param_ctx))

        return body


class Param:
    def __init__(self, target: Any, alias: str = None):
        self.target = target
        self.alias = alias or (
            target.__qualname__.split(".")[0]
            if hasattr(target, "__qualname__")
            else None
        )
        self.conflicts = 0

    def _target_ast(self, param_ctx: "ParamContext" = None) -> asttrs.stmt:
        value = self.target
        if isinstance(value, (type(None), bool, str, int, float)):  # early return
            return asttrs.Constant(value=value)

        if isinstance(value, List):
            return asttrs.List(
                elts=[
                    ParamContext.get(el, param_ctx)._target_ast(param_ctx)
                    for el in value
                ],
                ctx=asttrs.Load(),
            )

        if isinstance(value, Tuple):
            return asttrs.Tuple(
                elts=[
                    ParamContext.get(el, param_ctx)._target_ast(param_ctx)
                    for el in value
                ],
                ctx=asttrs.Load(),
            )

        if isinstance(value, Set):
            return asttrs.Set(
                elts=[
                    ParamContext.get(el, param_ctx)._target_ast(param_ctx)
                    for el in value
                ],
            )

        if isinstance(value, Dict):  # assume Dict[str, Any]
            return asttrs.Dict(
                keys=[asttrs.Constant(value=k) for k in value.keys()],
                values=[
                    ParamContext.get(el, param_ctx)._target_ast(param_ctx)
                    for el in value.values()
                ],
            )

        if isinstance(value, (MethodType, FunctionType, type)):
            if value.__name__ == "<lambda>":
                raise TypeError("lambda is not supported, please use function instead")

            name = value.__qualname__.split(".")
            name[0] = self.alias

            return asttrs.Name(id=".".join(name), ctx=asttrs.Load())

        if isinstance(value, Literal):
            return value._to_ast()

        raise TypeError(f"{type(value)} is not supported, got: {value}")

    def _dep_ast(self, param_ctx: "ParamContext" = None) -> List[asttrs.stmt]:
        body = []
        value = self.target

        if isinstance(value, (List, Tuple, Set)):
            for el in value:
                body.extend(ParamContext.get(el, param_ctx)._dep_ast(param_ctx))

        elif isinstance(value, Dict):  # assume Dict[str, Any]
            for v in value.values():
                body.extend(ParamContext.get(v, param_ctx)._dep_ast(param_ctx))

        elif isinstance(value, (MethodType, FunctionType, type)):
            if value.__name__ == "<lambda>":
                raise TypeError("lambda is not supported, please use function instead")

            modname = value.__module__
            name = value.__qualname__.split(".")[0]

            body.append(
                asttrs.ImportFrom(
                    module=modname,
                    names=[
                        asttrs.alias(
                            name=name, asname=None if name == self.alias else self.alias
                        )
                    ],
                )
            )

        elif isinstance(value, Literal):

            body.extend(value._dep_ast(param_ctx))

        return body


class ParamContext:

    def __init__(self):
        self.params: Dict[str, Param] = {}
        self.conflicts: Dict[str, int] = {}
        self.aliases: Dict[str, str] = {}

    @classmethod
    def get(cls, obj: Any, param_ctx: "ParamContext" = None) -> Param:
        return param_ctx._get(obj) if param_ctx else Param(obj)

    def _get(self, obj: Any) -> Param:
        if not isinstance(obj, (type, FunctionType, MethodType)):
            if isinstance(obj, (List, Tuple, Set)):
                for el in obj:
                    self._get(el)
            elif isinstance(obj, Dict):
                for el in obj.values():
                    self._get(el)

            return Param(obj)

        elif isinstance(obj, ModuleType):
            # TODO: module doesn't have __qualname__
            raise TypeError(f"ModuleType is not supported, got: {obj}")

        target_name = qualname(obj)
        qual_name = obj.__qualname__
        alias_name = qual_name.split(".")[0]
        import_name = f"{obj.__module__}.{alias_name}"

        if target_name in self.params:
            return self.params[target_name]

        if import_name in self.aliases:
            alias_name = self.aliases[import_name]

        else:
            alias_name = self._find_alias_without_conflict(alias_name)
            self.conflicts[alias_name] = 0
            self.aliases[import_name] = alias_name

        self.params[target_name] = Param(target=obj, alias=alias_name)

        return self.params[target_name]

    def _find_alias_without_conflict(self, name: str) -> str:
        curr, last = name, None
        while curr in self.conflicts:
            last = curr
            curr = f"{curr}_{self.conflicts[curr] + 1}"

        if last:
            self.conflicts[last] += 1

        return curr


class TaskAttribute:
    """
    Class representing a task attribute.

    Attributes:
        op_class (str | Type): The operator class associated with the task attribute. Defaults to "EmptyOperator".
        op_module (str): The module containing the operator class. Defaults to None.
        op_params (Dict[str, Any]): The parameters for the operator. Defaults to None.
        upstream (TaskClass | Iterable[TaskClass]): The upstream task(s) for this attribute. Defaults to None.
        downstream (TaskClass, Iterable[TaskClass]): The downstream task(s) for this attribute. Defaults to None.
    """

    op_class: Union[str, Type] = None
    op_module: Optional[str] = None
    op_params: Dict[str, Any] = None
    upstream: Optional[Union[TaskClass, Iterable[TaskClass]]] = None
    downstream: Optional[Union[TaskClass, Iterable[TaskClass]]] = None


class Task(TaskAttribute):

    @staticmethod
    def _get_taskid(cls) -> str:
        """Use qualified name as task_id
        Provide customized logic by overriding this method, and perhaps `_to_varname` as well.
        Please make sure the returned value is globally unique.
        """

        if (
            hasattr(cls, "_get_taskid")
            and
            # Assume classmethod
            inspect.ismethod(getattr(cls, "_get_taskid"))
        ):
            return cls._get_taskid()
        return qualname(cls)

    @staticmethod
    @lru_cache()
    def _get_attributes(cls) -> TaskAttribute:
        """Get and cache all the task's attributes.

        The expected attribute is defined in `TaskAttribute`,
        each attribute can be assign as a class variable or a @property,
        property precedes class variable if both are defined.

        In order to get the attribute from property, this method creates the task instance based on the Task class, make sure no positional arguments are required to create the task instance.

        """

        self: Union[Task, TaskClass] = None
        try:
            # Assume no arguments are required for creating the task instance.
            self = cls()
        except Exception:
            loguru.logger.warning(
                f"Cannot initialize {cls}, assume attributes are defined in class-var."
            )
            self = cls

        attrs = {}
        for field in TaskAttribute.__annotations__:
            value = getattr(self, field, None)

            if field == "op_class" and value is None:
                raise ValueError("op_class cannot be None")

            attrs[field] = value

        return immutable(TaskAttribute)(**attrs)

    @staticmethod
    def _to_varname(cls) -> str:
        """Represent the Task as a variable name
        The variable name is derived from task_id,
        if you change _get_taskid, you may need to change this method as well.
        """

        if (
            hasattr(cls, "_to_varname")
            and
            # Assume classmethod
            inspect.ismethod(getattr(cls, "_to_varname"))
        ):
            return cls._to_varname()

        return Task._get_taskid(cls).replace(".", "_")

    @staticmethod
    def _collect_dep_ast(cls, param_ctx: ParamContext = None) -> List[asttrs.stmt]:
        """Collect all stmts for all dependencies"""

        vendor_op = Task._resolve_operator(cls)
        op_modname, op_basename = qualname(vendor_op).rsplit(".", 1)
        op_modname = op_modname.replace("airfly._vendor.", "")

        deps = [
            asttrs.ImportFrom(module=op_modname, names=[asttrs.alias(name=op_basename)])
        ]

        params = Task._get_attributes(cls).op_params

        deps.extend(ParamContext.get(params, param_ctx)._dep_ast(param_ctx))

        return deps

    @staticmethod
    @lru_cache()
    def _collect_op_annotations(op: Type) -> Dict[str, Any]:
        """Collect annotations for the operator."""
        avai_params = {}

        if Task._is_builtin_op(op):
            for base in op.mro()[::-1]:
                avai_params.update(getattr(base, "__annotations__", {}))

        elif Task._is_private_op(op):
            for base in op.mro()[::-1]:
                signature = inspect.signature(base)
                for k, v in signature.parameters.items():

                    anno = v.annotation
                    if isinstance(anno, type):
                        typename = qualname(anno, level=1)
                    elif hasattr(anno, "__module__") and anno.__module__ == "typing":
                        typename = str(anno)
                    elif isinstance(anno, str):
                        typename = anno
                    else:
                        raise TypeError(f"got: {anno}")

                    if v.kind not in [
                        inspect._ParameterKind.VAR_KEYWORD,
                        inspect._ParameterKind.VAR_POSITIONAL,
                    ]:

                        avai_params.update({k: typename})
        else:
            raise ValueError(f"Operator {op} is not supported.")

        return avai_params

    @staticmethod
    def _to_ast(
        cls, param_ctx: ParamContext = None, task_group: bool = True
    ) -> asttrs.AST:
        """
        Generate an Abstract Syntax Tree (AST) representation of the Task.

        Returns:
            asttrs.AST: The AST representation of the Task.

        Notes:
            - This method uses the `asttrs` module for creating the AST nodes.
            - The AST represents the assignment of a Task instance to a variable.
            - The Task instance is created by calling the resolved operator class with the appropriate parameters.
            - The parameters are obtained from the Task's attributes and the operator's available parameters.
            - The AST node is an assignment statement, where the target is the variable name and the value is the function call.

        # TODO: Add unit tests for this method.
        """

        op = Task._resolve_operator(cls)
        op_basename = qualname(op, level=1)

        task_id = Task._get_taskid(cls)
        task_varname = Task._to_varname(cls)

        avai_params = Task._collect_op_annotations(op)
        params = dict(task_id=task_id)

        for k, v in (Task._get_attributes(cls).op_params or {}).items():
            if k in params:
                loguru.logger.warning(f"Overwrite param {k}={params[k]} with value {v}")
            if k in avai_params:
                params.update({k: v})
            else:
                loguru.logger.warning(f"Ingore invalid param: {k} in {cls}.")

        keywords = []

        for k, v in params.items():
            par = ParamContext.get(v, param_ctx)
            keywords.append(asttrs.keyword(arg=k, value=par._target_ast(param_ctx)))

        if task_group:
            group_id = task_id.rsplit(".", 1)[0]
            group_var = TaskGroup._to_varname(group_id)
            keywords.append(
                asttrs.keyword(
                    arg="task_group",
                    value=asttrs.Name(id=group_var, ctx=asttrs.Load()),
                )
            )

        assign = asttrs.Assign(
            targets=[asttrs.Name(id=task_varname, ctx=asttrs.Store())],
            value=asttrs.Call(
                func=asttrs.Name(id=op_basename, ctx=asttrs.Load()),
                keywords=keywords,
            ),
        )

        return assign

    @staticmethod
    @lru_cache()
    def _is_builtin_op(op: Type) -> bool:
        return issubclass_by_qualname(op, BUILTIN_OPERATORS["BaseOperator"])

    @staticmethod
    @lru_cache()
    def _is_private_op(op: Type) -> bool:
        try:
            from airflow.models.baseoperator import BaseOperator

            return issubclass_by_qualname(op, BaseOperator)
        except Exception as err:
            loguru.logger.warning(f"{err.__class__}: {err}")
            pass

        return False

    @staticmethod
    def _resolve_operator(cls) -> Type:
        """Resolve the operator class for the Task.

        Returns:
            Type: The resolved operator class.

        Raises:
            ValueError: If the op_class is invalid or not found in the BUILTIN_OPERATORS.
            ValueError: If multiple op_class with the same basename are found and op_module is not provided or invalid.
            ValueError: If the op_class candidates cannot be resolved by the given op_module.
        """

        op_class = Task._get_attributes(cls).op_class

        if isinstance(op_class, type):

            if Task._is_builtin_op(op_class) or Task._is_private_op(op_class):
                return op_class

            raise TypeError(f"Not a valid operator type, got: {op_class}")

        # NOTE: if op_class is str, assume it's a builtin operator
        if isinstance(op_class, str):
            basename = op_class

        else:
            raise ValueError(f"Invalid op_class, got: {op_class}")

        if basename not in BUILTIN_OPERATORS:
            raise ValueError(
                f"'{basename}' not found. If this is unexpected and the operator should exist, please report the issue."
            )
        items = BUILTIN_OPERATORS[basename]

        if len(items) > 1:
            # Disambiguate by op_module
            op_module = Task._get_attributes(cls).op_module
            if not (op_module and isinstance(op_module, str)):
                raise ValueError(
                    f"Multiple op_class('{basename}') found: {items}, but op_module is invalid for resolving the operator, got: {op_module}"
                )

            cands = [op for op in items if op_module in qualname(op)]

            if len(cands) != 1:
                raise ValueError(
                    f"Cannot resolve the possible op_class('{basename}') by given op_module('{op_module}'), multiple or no candidates found: {cands}"
                )

            items = cands

        return items[0]


class AirFly(Task): ...


@immutable
class TaskPair:
    """
    A class representing a pair of tasks.

    Attributes:
        up (TaskClass): The class representing the 'up' task.
        down (TaskClass): The class representing the 'down' task.

    """

    up: TaskClass
    down: TaskClass

    def _to_ast(self) -> asttrs.AST:
        """Returns an Abstract Syntax Tree (AST) representation of the TaskPair.

        i.e., an AST to represent an expression: "up_task >> down_task"

        This method generates an AST that represents the TaskPair as a binary operation expression. The left operand of the binary operation is the result of calling the '_to_varname' method on the 'up' task, and the right operand is the result of calling the '_to_varname' method on the 'down' task.

        Returns:
            asttrs.AST: The AST representation of the TaskPair.

        """

        return asttrs.Expr(
            value=asttrs.BinOp(
                left=asttrs.Name(id=Task._to_varname(self.up), ctx=asttrs.Store()),
                op=asttrs.RShift(),
                right=asttrs.Name(id=Task._to_varname(self.down), ctx=asttrs.Load()),
            )
        )


@immutable
class TaskGroup:
    group_id: str
    parent_id: str = None

    def _to_ast(self) -> asttrs.stmt:
        keywords = [
            asttrs.keyword(arg="group_id", value=asttrs.Constant(value=self.group_id)),
            asttrs.keyword(arg="prefix_group_id", value=asttrs.Constant(value=False)),
        ]

        if self.parent_id:
            keywords.append(
                asttrs.keyword(
                    arg="parent_group",
                    value=asttrs.Name(
                        id=self._to_varname(self.parent_id), ctx=asttrs.Load()
                    ),
                )
            )

        return asttrs.Assign(
            targets=[
                asttrs.Name(id=self._to_varname(self.group_id), ctx=asttrs.Store())
            ],
            value=asttrs.Call(
                func=asttrs.Name(id="TaskGroup", ctx=asttrs.Load()),
                keywords=keywords,
            ),
        )

    @classmethod
    def _to_varname(cls, group_id) -> str:
        return "group_" + group_id.replace(".", "_")


@immutable
class TaskTree:
    """A class representing a task tree.

    The TaskTree class represents a task tree, which consists of a set of task classes and a set of task pairs. The task classes are collected from a module based on certain criteria, such as being a subclass of a base task class and satisfying a predicate function. The task pairs represent the dependencies between tasks.

    Attributes:
        taskset (Set[TaskClass]): The set of task classes in the task tree.
        taskpairs (Set[TaskPair]): The set of task pairs in the task tree.

    Methods:
        from_module(module: ModuleType) -> TaskTree:
            Creates a task tree from a module.
            This method takes a module as input and creates a task tree from it. The task tree consists of a set of task classes and a set of task pairs. The task classes are collected from the module based on certain criteria, such as being a subclass of a base task class and satisfying a predicate function. The task pairs are generated from the task classes, representing the dependency between tasks.

        to_source() -> str:
            Generates the source code representation of the task tree.
            This method generates the source code representation of the task tree, including the import statements, class definition, and task pair expressions.

    Example:
    >>> TaskTree.from_module(module).to_source(formatted=True)

    Note:
        - The TaskTree class is immutable, meaning that its attributes cannot be modified after initialization.
        - The taskset attribute is a set of task classes, where each task class represents a task in the task tree.
        - The taskpairs attribute is a set of task pairs, where each task pair represents a dependency between two tasks in the task tree.
        - The _dag attribute is a directed graph (DiGraph) object from the NetworkX library, which represents the task tree as a directed acyclic graph (DAG).
        - The from_module method is a class method that creates a task tree from a module.
        - The to_source method generates the source code representation of the task tree, which can be used to create a Python script or module.
    """

    taskset: Set[TaskClass]
    taskpairs: Set[TaskPair]

    _dag: nx.DiGraph = attr.ib(init=False)

    @_dag.default
    def _create_dag(self):
        dag = nx.DiGraph()
        dag.add_nodes_from(self.taskset)
        dag.add_edges_from((pair.up, pair.down) for pair in self.taskpairs)

        return dag

    @classmethod
    def from_module(
        cls, module: ModuleType, taskclass: type = AirFly, exclude_pattern: str = None
    ) -> "TaskTree":
        """
        Creates a task tree from a module.

        This method takes a module as input and creates a task tree from it. The task tree consists of a set of task classes and a set of task pairs. The task classes are collected from the module based on certain criteria, such as being a subclass of a base task class and satisfying a predicate function. The task pairs are generated from the task classes, representing the dependency between tasks.

        Parameters:
            module (ModuleType): The module from which to create the task tree.

        Returns:
            TaskTree: The task tree created from the module.

        Example:
            >>> module = ...
            >>> task_tree = TaskTree.from_module(module)

        # TODO: add predicate in argument
        """

        loguru.logger.info(
            f"Collecting '{qualname(taskclass)}' from '{qualname(module)}' ..."
        )
        taskset = set(
            cls._collect_taskclass(
                module,
                taskclass,
                predicate=lambda obj: not cls._should_exclude(obj, exclude_pattern),
            )
        )
        taskpairs = set(
            cls._collect_taskpairs(
                taskset,
                taskclass,
                predicate=lambda pair: not (
                    cls._should_exclude(
                        pair.up,
                        exclude_pattern,
                    )
                    or cls._should_exclude(
                        pair.down,
                        exclude_pattern,
                    )
                ),
            )
        )

        return cls(taskset=taskset, taskpairs=taskpairs)

    @classmethod
    def _should_exclude(
        cls,
        obj: Union[FunctionType, type],
        pattern: Optional[str] = None,
    ):
        if pattern and isinstance(pattern, str):
            obj_name = qualname(obj)
            if re.search(pattern, obj_name):
                return True

        return False

    @classmethod
    def _collect_taskclass(
        cls, module: ModuleType, taskclass: TaskClass = Task, predicate=lambda _: True
    ) -> Generator[TaskClass, None, None]:
        """
        Collects task classes from a module.

        This method collects task classes from a given module based on the provided criteria. It returns a generator that yields the task classes.

        Parameters:
            module (ModuleType): The module from which to collect the task classes.
            taskclass (Type["Task"], optional): The base task class to filter the task classes. Defaults to Task.
            predicate (Callable[[Union[FunctionType, type]], bool], optional): A predicate function to further filter the task classes. Defaults to lambda _: True.

        Yields:
            TaskClass: The task classes that satisfy the filtering criteria.

        Example:
            >>> module = ...
            >>> task_classes = list(TaskTree._collect_taskclass(module))
        """
        for cls in collect_objects(
            module,
            predicate=lambda obj: isinstance(obj, type)
            and issubclass_by_qualname(obj, taskclass)
            and predicate(obj),
        ):

            yield cls

    @classmethod
    def _collect_taskpairs(
        cls,
        taskset: Set[TaskClass],
        taskclass: TaskClass = Task,
        predicate=lambda _: True,
    ) -> Generator[TaskPair, None, None]:
        """
        Collects task pairs from a given task set.

        This method takes a set of task classes and collects all possible pairs of tasks based on the provided criteria. It returns a generator that yields the task pairs.

        Parameters:
            taskset (Set[TaskClass]): The set of task classes from which to collect the task pairs.
            taskclass (TaskClass): The base task class to filter the task pairs. Defaults to Task.
            predicate (Callable[[TaskPair], bool], optional): A predicate function to further filter the task pairs. Defaults to lambda _: True.

        Yields:
            TaskPair: The task pairs that satisfy the filtering criteria.

        Example:
            >>> taskset = {Task1, Task2, Task3}
            >>> task_pairs = list(TaskTree._collect_taskpairs(taskset))
        """

        cached = set()

        for cls in taskset:
            ups = Task._get_attributes(
                cls
            ).upstream  # could be None, Task or Iterable[Task, ...]

            if isinstance(ups, type) and issubclass_by_qualname(ups, taskclass):
                ups = [ups]

            for u in ups or []:

                if isinstance(u, type) and issubclass_by_qualname(u, taskclass):
                    pair = TaskPair(up=u, down=cls)

                    if (pair not in cached) and predicate(pair):
                        cached.add(pair)

                        yield pair

            downs = Task._get_attributes(
                cls
            ).downstream  # could be None, Task or Tuple[Task, ...]

            if isinstance(downs, type) and issubclass_by_qualname(downs, taskclass):
                downs = [downs]

            for d in downs or []:

                if isinstance(d, type) and issubclass_by_qualname(d, taskclass):
                    pair = TaskPair(up=cls, down=d)

                    if pair not in cached and predicate(pair):
                        cached.add(pair)

                        yield pair

    def to_dag(
        self,
        name: str,
        includes: Union[str, List[str]] = None,
        dag_params: Tuple[str, str] = None,
        task_group: bool = True,
        formatted: bool = True,
    ) -> str:
        """Generates the source code representation of the task tree.

        This method generates the source code representation of the task tree by converting the abstract syntax tree (AST) of the task tree to source code. The AST is obtained by calling the `_to_ast` method. The source code is then passed through the `blacking` and `isorting` functions to format and sort the code, respectively.

        Parameters:
            formatted (bool, optional): Specifies whether the generated source code should be formatted. If `True`, the code will be formatted using the `blacking` and `isorting` functions. If `False`, the code will be returned as is. Defaults to `True`.

        Returns:
            str: The source code representation of the task tree.

        Note:
            - The `formatted` parameter determines whether the generated source code should be formatted. If `True`, the code will be formatted using the `blacking` and `isorting` functions. If `False`, the code will be returned as is.
            - The `blacking` function is used to format the code by applying the `black` code formatter.
            - The `isorting` function is used to sort the imports in the code by applying the `isort` import sorter.
            - The `re.sub` function is used to remove any consecutive newline characters in the source code.

        Example:
            >>> task_tree = TaskTree(...)
            >>> source_code = task_tree.to_source(formatted=True)
        """

        loguru.logger.info(
            f"Generating code of dag.py: name='{name}', includes={includes}, dag_params={dag_params}"
        )

        src = re.sub(
            "\n+",
            "\n",
            self._to_ast(name, dag_params, includes, task_group).to_source(),
        )

        return isorting(blacking(src)) if formatted else src

    def _to_ast(
        self,
        dag_name,
        dag_params,
        includes,
        task_group=True,
    ) -> asttrs.AST:

        ctx = ParamContext()
        body = (
            self._build_header()
            + self._build_imports(task_group)
            + self._build_includes(includes)
            + self._build_dag_context(
                dag_name=dag_name,
                dag_params=dag_params,
                param_ctx=ctx,
                task_group=task_group,
            )
        )

        return asttrs.Module(body=body)

    def _build_header(self) -> List[asttrs.stmt]:

        return [
            asttrs.Comment(
                body=f"This file is auto-generated by {airfly.__name__} {airfly.__version__}"
            )
        ]

    def _build_imports(self, task_group=True) -> List[asttrs.stmt]:

        imports = [
            asttrs.ImportFrom(module="airflow.models", names=[asttrs.alias(name="DAG")])
        ]

        if task_group:
            imports.append(
                asttrs.ImportFrom(
                    module="airflow.utils.task_group",
                    names=[asttrs.alias(name="TaskGroup")],
                )
            )

        return imports

    def _build_includes(
        self, includes: Union[str, List[str]] = None
    ) -> List[asttrs.stmt]:
        if includes:
            if isinstance(includes, str):
                includes = [includes]

            imports = []
            statements = []

            for path in includes:
                for st in self._insert_from_pyfile(path):
                    if isinstance(st, (asttrs.Import, asttrs.ImportFrom)):
                        if st not in imports:
                            imports.append(st)
                    else:
                        statements.append(st)

            body = (
                imports
                + statements
                + [asttrs.Comment(body="<" * 10 + " End of code insertion")]
            )

            return body

        return []

    def _insert_from_pyfile(self, path: str) -> List[asttrs.stmt]:

        try:

            if os.path.isfile(path):
                mod: asttrs.Module = asttrs.Module.from_file(path)
                mod.body.insert(
                    0, asttrs.Comment(body=">" * 10 + f" Include from '{path}'")
                )

                return mod.body

        except Exception as e:
            loguru.logger.warning(f"Ignore failed insert from '{path}': {e}")
            pass

        return []

    def _build_dag_context(
        self,
        dag_name: str,
        dag_params: Tuple[str, str] = None,
        param_ctx=None,
        task_group=True,
    ) -> List[asttrs.stmt]:

        if dag_params and dag_params[1]:
            _, param_var = dag_params
            keywords = [
                asttrs.keyword(
                    arg=None,
                    value=asttrs.Name(id=param_var, ctx=asttrs.Load()),
                )
            ]
        else:
            keywords = []

        return [
            asttrs.With(
                items=[
                    asttrs.withitem(
                        context_expr=asttrs.Call(
                            func=asttrs.Name(id="DAG", ctx=asttrs.Load()),
                            args=[asttrs.Constant(value=dag_name)],
                            keywords=keywords,
                        ),
                        optional_vars=asttrs.Name(id="dag", ctx=asttrs.Store()),
                    )
                ],
                body=self._build_dag_body(param_ctx=param_ctx, task_group=task_group),
            )
        ]

    def _build_dag_body(self, param_ctx=None, task_group=True) -> List[asttrs.stmt]:
        body = []

        for cls in self.taskset:
            for st in Task._collect_dep_ast(cls, param_ctx):
                if st not in body:
                    body.append(st)

        if task_group:
            body.extend(self._build_task_group())

        for cls in sorted(self.taskset, key=lambda el: qualname(el)):
            body.append(Task._to_ast(cls, param_ctx, task_group))

        for pair in sorted(
            self.taskpairs,
            key=lambda el: f"{qualname(el.up)}{qualname(el.down)}",
        ):

            body.append(pair._to_ast())

        return body if body else [asttrs.Pass()]

    def _build_task_group(self) -> List[asttrs.stmt]:

        body = []
        group_ids = sorted(
            {Task._get_taskid(cls).rsplit(".", 1)[0] for cls in self.taskset}
        )

        tree = {}
        for gid in group_ids:
            node = tree
            for path in gid.split("."):
                if path not in node:
                    node[path] = {}
                node = node[path]

        todo = deque([(tree, [])])
        while todo:
            root, prefix = todo.popleft()

            for k, node in root.items():
                gid = ".".join(prefix + [k])
                body.append(
                    TaskGroup(
                        group_id=gid, parent_id=".".join(prefix) if prefix else None
                    )._to_ast()
                )

                todo.append((node, prefix + [k]))

        return body
