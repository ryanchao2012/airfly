from functools import lru_cache
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union

from airfly._vendor import collect_airflow_operators
from airfly.utils import immutable, qualname

TaskClass = Type["Task"]


AVAILABLE_OPERATORS = collect_airflow_operators()


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

    @classmethod
    def _get_taskid(cls) -> str:
        """Use qualified name as task_id
        Provide customized logic by overriding this method, and perhaps `_to_varname` as well.
        Please make sure the returned value is globally unique.
        """
        return qualname(cls)

    @classmethod
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
        for field in cls.__annotations__:
            value = getattr(self, field, None) or getattr(cls, field, None)

            if field == "op_class" and value is None:
                raise ValueError("op_class cannot be None")

            attrs[field] = value

        return immutable(TaskAttribute)(**attrs)

    @classmethod
    def _to_varname(cls) -> str:
        """Represent the Task as a variable name
        The variable name is derived from task_id,
        if you change _get_taskid, you may need to change this method as well.
        """

        return cls._get_taskid().replace(".", "_")

    @classmethod
    def _to_ast(cls): ...

    @classmethod
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

        op_class = cls._get_attributes().op_class

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
            op_module = cls._get_attributes().op_module
            if not (op_module and isinstance(op_module, str)):
                raise ValueError(
                    f"Multiple op_class('{basename}') found: {items}, but op_module is invalid for resolving the operator, got: {op_module}"
                )

            for op in items:
                if op_module in qualname(op):
                    return op

            raise ValueError(
                f"Cannot resolve the possible op_class('{items}') by given op_module, got: {op_module}"
            )

        return items[0]


AirFly: Type = Task


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

    @classmethod
    def _to_ast(cls): ...


class TaskTree:
    """
    A class representing a task tree.

    The TaskTree class provides methods for creating a task tree from a module, collecting task sets and task pairs, and generating source code from the task tree.

    Attributes:
        None

    Methods:
        from_module(cls, modname: str) -> TaskTree: Creates a task tree from a module.
        to_source(self) -> str: Generates source code from the task tree.

    Example:
    >>> TaskTree.from_module(modname).to_source(formatted=True)
    """

    @classmethod
    def from_module(cls, modname: str): ...

    @classmethod
    def _collect_taskset(cls): ...
    @classmethod
    def _collect_taskpairs(cls): ...

    def to_source(self) -> str: ...

    def _to_ast(self): ...

    def _build_header(self): ...

    def _build_imports(self): ...

    def _build_includes(self): ...

    def _build_dag_context(self): ...
