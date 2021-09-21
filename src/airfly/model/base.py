from types import ModuleType
from typing import Generator, List, Sequence, Set, Tuple, Type, Union

import attr
import networkx as nx
from airfly._ast import immutable
from airfly.utils import collect_objects

TaskClass = Type["BaseTask"]


class BaseTask:
    upstreams: Union[Tuple[TaskClass, ...], TaskClass] = None
    downstreams: Union[Tuple[TaskClass, ...], TaskClass] = None


@immutable
class TaskPair:
    up: TaskClass
    down: TaskClass


@immutable
class TaskTree:

    taskset: Set[BaseTask]
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
    module: ModuleType, taskclass: TaskClass = BaseTask, predicate=lambda _: True
) -> Generator[TaskClass, None, None]:

    for cls in collect_objects(
        module,
        predicate=lambda obj: isinstance(obj, type)
        and issubclass(obj, taskclass)
        and predicate(obj),
    ):

        yield cls  # return task class with no duplication


def collect_taskpairs(
    taskset: Set[TaskClass], taskclass: TaskClass = BaseTask, predicate=lambda _: True
) -> Generator[TaskPair, None, None]:

    cached = set()

    for cls in taskset:

        ups = cls.upstreams  # could be None, Task or Tuple[Task, ...]

        if isinstance(ups, type) and issubclass(ups, taskclass):
            ups = [ups]

        for u in ups or []:

            pair = TaskPair(up=u, down=cls)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair

        downs = cls.downstreams  # could be None, Task or Tuple[Task, ...]

        if isinstance(downs, type) and issubclass(downs, taskclass):
            downs = [downs]

        for d in downs or []:

            pair = TaskPair(up=cls, down=d)

            if pair not in cached and predicate(pair):

                cached.add(pair)

                yield pair


class Workflow:
    def to_source(self) -> str:
        raise NotImplementedError

    def to_file(self, path: str):
        pass
