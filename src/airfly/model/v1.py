from typing import Any, Dict, Optional, Tuple, Type, Union

from airfly.utils import immutable, qualname

TaskClass = Type["Task"]


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
    downstream = Optional[Union[TaskClass, Tuple[TaskClass, ...]]] = None


class Task(TaskAttribute):

    @classmethod
    def _get_taskid(cls) -> str:
        """Use qualified name as task_id
        Provide customized logic by overriding this method.
        However, please make sure the returned value is globally unique.
        """
        return qualname(cls)

    @classmethod
    def _get_attributes(cls): ...

    @classmethod
    def _to_varname(cls): ...

    @classmethod
    def _to_ast(cls): ...

    @classmethod
    def _resolve_operator(cls) -> Type: ...


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
