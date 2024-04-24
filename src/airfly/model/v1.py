import inspect
import os
from functools import lru_cache
from types import FunctionType, MethodType, ModuleType
from typing import Any, Dict, Generator, List, Optional, Set, Tuple, Type, Union

import asttrs
import attr
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


AVAILABLE_OPERATORS = collect_airflow_operators()


class Literal:

    def __init__(self, expr: str, refs: List[Any] = None, aliases: List[str] = None):
        self.expr = expr
        self.refs = refs if isinstance(refs, List) else [refs]
        self.aliases = aliases if isinstance(aliases, List) else [aliases]

    def __repr__(self):
        return self.expr


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
        if isinstance(
            value, (type(None), bool, str, int, float, Literal)
        ):  # early return
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
                raise NotImplementedError("can't support lambda, use function instead")

            name = value.__qualname__.split(".")
            name[0] = self.alias

            return asttrs.Name(id=".".join(name), ctx=asttrs.Load())

        return asttrs.Constant(value=value)

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
                raise NotImplementedError("not support lambda, use function instead")

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
            raise TypeError(f"can't support ModuleType, got: {obj}")

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
        upstream (TaskClass | Tuple[TaskClass, ...]): The upstream task(s) for this attribute. Defaults to None.
        downstream (TaskClass, Tuple[TaskClass, ...]): The downstream task(s) for this attribute. Defaults to None.
    """

    op_class: Union[str, Type] = None
    op_module: Optional[str] = None
    op_params: Dict[str, Any] = None
    upstream: Optional[Union[TaskClass, Tuple[TaskClass, ...]]] = None
    downstream: Optional[Union[TaskClass, Tuple[TaskClass, ...]]] = None


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
    def _get_taskgroup(cls) -> "TaskGroup":
        if (
            hasattr(cls, "_get_taskgroup")
            and
            # Assume classmethod
            inspect.ismethod(getattr(cls, "_get_taskgroup"))
        ):
            return cls._get_taskid()

        group_id = Task._get_taskid(cls).rsplit(".", 1)[0]
        if "." in group_id:
            parent_group_id = group_id.rsplit(".", 1)[0]
            parent_group = TaskGroup(group_id=parent_group_id)
        else:
            parent_group = None

        return TaskGroup(group_id=group_id, parent_group=parent_group)

    @staticmethod
    @lru_cache()
    def _get_attributes(cls) -> TaskAttribute:
        """Get and cache all the task's attributes.

        The expected attribute is defined in `TaskAttribute`,
        each attribute can be assign as a class variable or a @property,
        property precedes class variable if both are defined.

        In order to get the attribute from property, this method creates the task instance based on the Task class, make sure no positional arguments are required to create the task instance.

        """

        self: Task = None
        try:
            # Assume no arguments are required for creating the task instance.
            self = cls()
        except Exception:
            # TODO: logging warning
            pass

        attrs = {}
        for field in TaskAttribute.__annotations__:
            value = getattr(self, field, None) or getattr(cls, field, None)

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

        TODO:
            - Add unit tests for this method.
        """

        op = Task._resolve_operator(cls)
        op_basename = qualname(op, level=1)

        task_id = Task._get_taskid(cls)
        task_varname = Task._to_varname(cls)

        avai_params = {}
        for base in op.mro()[::-1]:
            avai_params.update(getattr(base, "__annotations__", {}))

        params = dict(task_id=task_id)

        for k, v in (Task._get_attributes(cls).op_params or {}).items():
            if k in avai_params:
                params.update({k: v})
            else:
                # TODO: logging
                ...

        keywords = []
        if task_group:
            keywords.append(
                asttrs.keyword(
                    arg="task_group",
                    value=asttrs.Name(
                        id=Task._get_taskgroup(cls)._to_varname(), ctx=asttrs.Load()
                    ),
                )
            )

        for k, v in params.items():

            par = ParamContext.get(v, param_ctx)
            keywords.append(asttrs.keyword(arg=k, value=par._target_ast(param_ctx)))

        assign = asttrs.Assign(
            targets=[asttrs.Name(id=task_varname, ctx=asttrs.Store())],
            value=asttrs.Call(
                func=asttrs.Name(id=op_basename, ctx=asttrs.Load()),
                keywords=keywords,
            ),
        )

        return assign

    @staticmethod
    def _resolve_operator(cls) -> Type:
        """Resolve the operator class for the Task.

        Returns:
            Type: The resolved operator class.

        Raises:
            ValueError: If the op_class is invalid or not found in the AVAILABLE_OPERATORS.
            ValueError: If multiple op_class with the same basename are found and op_module is not provided or invalid.
            ValueError: If the op_class candidates cannot be resolved by the given op_module.

        TODO:
            - Add unit tests for this method.
        """
        # TODO: unittest

        op_class = Task._get_attributes(cls).op_class

        if isinstance(op_class, type):

            if issubclass_by_qualname(op_class, AVAILABLE_OPERATORS["BaseOperator"]):
                return op_class

            raise TypeError(f"Not a valid operator type, got: {op_class}")

        if isinstance(op_class, str):
            basename = op_class

        elif isinstance(op_class, type):
            basename = qualname(op_class, level=1)

        else:
            raise ValueError(f"Invalid op_class, got: {op_class}")

        if basename not in AVAILABLE_OPERATORS:
            raise ValueError(
                f"'{basename}' not found. If this is unexpected and the operator should exist, please report the issue."
            )
        items = AVAILABLE_OPERATORS[basename]

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
    parent_group: Optional["TaskGroup"] = None

    @property
    def prefix(self):
        return "group"

    def _to_ast(self) -> asttrs.stmt:
        keywords = [
            asttrs.keyword(arg="group_id", value=asttrs.Constant(value=self.group_id)),
            asttrs.keyword(arg="prefix_group_id", value=asttrs.Constant(value=False)),
        ]

        if self.parent_group:
            keywords.append(
                asttrs.keyword(
                    arg="parent_group",
                    value=asttrs.Name(
                        id=self.parent_group._to_varname(), ctx=asttrs.Load()
                    ),
                )
            )

        return asttrs.Assign(
            targets=[asttrs.Name(id=self._to_varname(), ctx=asttrs.Store())],
            value=asttrs.Call(
                func=asttrs.Name(id="TaskGroup", ctx=asttrs.Load()),
                keywords=keywords,
            ),
        )

    def _to_varname(self) -> str:
        return self.prefix + "_" + self.group_id.replace(".", "_")


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

        TODO: add predicate in argument
        """

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
            ).upstream  # could be None, Task or Tuple[Task, ...]

            if isinstance(ups, type) and issubclass_by_qualname(ups, taskclass):
                ups = [ups]

            for u in ups or []:

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

                pair = TaskPair(up=cls, down=d)

                if pair not in cached and predicate(pair):

                    cached.add(pair)

                    yield pair

    def to_dag(
        self,
        name: str,
        includes: Union[str, List[str]] = None,
        dag_params: Tuple[str, str] = None,
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

        src = re.sub("\n+", "\n", self._to_ast(name, dag_params, includes).to_source())

        return isorting(blacking(src)) if formatted else src

    def _to_ast(
        self,
        dag_name,
        dag_params,
        includes,
    ) -> asttrs.AST:

        ctx = ParamContext()
        body = (
            self._build_header()
            + self._build_imports(ctx)
            + self._build_includes(includes)
            + self._build_dag_context(
                dag_name=dag_name, dag_params=dag_params, param_ctx=ctx
            )
        )

        return asttrs.Module(body=body)

    def _build_header(self) -> List[asttrs.stmt]:

        return [
            asttrs.Comment(
                body=f"This file is auto-generated by {airfly.__name__} {airfly.__version__}"
            )
        ]

    def _build_imports(self, param_ctx: ParamContext = None) -> List[asttrs.stmt]:

        imports = [
            asttrs.ImportFrom(module="airflow.models", names=[asttrs.alias(name="DAG")])
        ]

        for cls in self.taskset:
            for st in Task._collect_dep_ast(cls, param_ctx):
                if st not in imports:
                    imports.append(st)

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

        except Exception:
            # TODO: logging?
            pass

        return []

    def _build_dag_context(
        self, dag_name: str, dag_params: Tuple[str, str] = None, param_ctx=None
    ) -> List[asttrs.stmt]:

        if dag_params:
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
                body=self._build_dag_body(param_ctx=param_ctx),
            )
        ]

    def _build_dag_body(self, param_ctx=None) -> List[asttrs.stmt]:
        body = []

        for cls in sorted(self.taskset, key=lambda el: qualname(el)):
            body.append(Task._to_ast(cls, param_ctx))

        for pair in sorted(
            self.taskpairs,
            key=lambda el: f"{qualname(el.up)}{qualname(el.down)}",
        ):

            body.append(pair._to_ast())

        return body if body else [asttrs.Pass()]
