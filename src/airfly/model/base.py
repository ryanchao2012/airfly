from functools import lru_cache
from types import ModuleType
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

import attr
import networkx as nx
import regex as re

from airfly.utils import collect_objects, qualname

immutable = attr.s(auto_attribs=True, slots=True, frozen=True, kw_only=True)


TaskClass = Type["Task"]


class TaskAttribute:
    """

    Attribute can be assigned as class variable or property:
    - task_id:
    - op_class:
    - op_module:
    - op_params:
    - upstream:
    - downstream:
    """

    task_id: str = None  # NOTE: if not given, we will use qualname() to assign task_id
    op_class: Union[Type, str] = "EmptyOperator"

    # TODO: disambiguate operator as op_class collision
    op_module: Union[ModuleType, str] = None
    op_params: Dict[str, Any] = None

    upstream: Union[TaskClass, Tuple[TaskClass, ...]] = None
    downstream: Union[TaskClass, Tuple[TaskClass, ...]] = None


class Task(TaskAttribute):

    @property
    def task_id(self):
        return qualname(self.__class__)

    @classmethod
    def to_varname(cls):
        return re.sub("\W|^(?=\d)", "_", cls.get_attributes().task_id)

    @classmethod
    @lru_cache()
    def get_attributes(cls, **kwargs) -> TaskAttribute:

        self = cls(**kwargs)

        attrs = {}
        for field in cls.__annotations__:
            value = getattr(self, field, None) or getattr(cls, field, None)

            if value is None:
                # TODO: logging
                ...

            elif isinstance(value, Callable):
                value = value(**kwargs)

            attrs[field] = value

        return immutable(TaskAttribute)(**attrs)


@immutable
class TaskPair:
    up: TaskClass
    down: TaskClass


@immutable
class TaskTree:

    taskset: Set[TaskClass]
    taskpairs: Set[TaskPair]

    _dag: nx.DiGraph = attr.ib(init=False)

    @_dag.default
    def _create_dag(self):
        dag = nx.DiGraph()
        dag.add_nodes_from(self.taskset)
        dag.add_edges_from((pair.up, pair.down) for pair in self.taskpairs)

        return dag

    @property
    def roots(self) -> List[TaskClass]:
        return [node for node in self._dag.nodes() if self._dag.in_degree(node) == 0]

    @property
    def leaves(self) -> List[TaskClass]:
        return [node for node in self._dag.nodes() if self._dag.out_degree(node) == 0]

    @property
    def nodes(self) -> Sequence[TaskClass]:
        return self._dag.nodes

    @property
    def edges(self) -> Sequence[Tuple[TaskClass, TaskClass]]:
        return self._dag.edges


def collect_taskset(
    module: ModuleType,
    taskclass: TaskClass = Task,
    predicate=lambda _: True,
) -> Generator[TaskClass, None, None]:

    for cls in collect_objects(
        module,
        predicate=lambda obj: isinstance(obj, type)
        and issubclass(obj, taskclass)
        and predicate(obj),
    ):

        yield cls  # return task class with no duplication


def collect_taskpairs(
    taskset: Set[TaskClass], taskclass: TaskClass = Task, predicate=lambda _: True
) -> Generator[TaskPair, None, None]:

    cached = set()

    for cls in taskset:

        ups = cls.get_attributes().upstream

        if isinstance(ups, type) and issubclass(ups, taskclass):
            ups = [ups]

        for u in ups or []:

            pair = TaskPair(up=u, down=cls)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair

        downs = cls.get_attributes().downstream

        if isinstance(downs, type) and issubclass(downs, taskclass):
            downs = [downs]

        for d in downs or []:

            pair = TaskPair(up=cls, down=d)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair
