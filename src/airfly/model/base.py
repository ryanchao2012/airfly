from types import ModuleType
from typing import Generator, List, Sequence, Set, Tuple, Type, Union

import attr
import networkx as nx

from airfly.utils import collect_objects

immutable = attr.s(auto_attribs=True, slots=True, frozen=True, kw_only=True)


TaskClass = Type["Task"]


class Task:
    task_id: str = None  # NOTE: if not given, we will use qualname() to assign task_id
    upstream: Union[TaskClass, Tuple[TaskClass, ...]] = None
    downstream: Union[TaskClass, Tuple[TaskClass, ...]] = None


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
        # TODO: if upstream is a property, try create task instance(cls()) to get them
        ups = cls.upstream  # could be None, Task or Tuple[Task, ...]

        if isinstance(ups, type) and issubclass(ups, taskclass):
            ups = [ups]

        for u in ups or []:

            pair = TaskPair(up=u, down=cls)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair

        # TODO: if downstream is a property, try create task instance(cls()) to get them
        downs = cls.downstream  # could be None, Task or Tuple[Task, ...]

        if isinstance(downs, type) and issubclass(downs, taskclass):
            downs = [downs]

        for d in downs or []:

            pair = TaskPair(up=cls, down=d)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair
