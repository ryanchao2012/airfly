from types import ModuleType
from typing import Generator, List, Sequence, Set, Tuple, Type, Union

import networkx as nx
from airfly._ast import immutable
from airfly.utils import collect_objects, qualname

TaskClass = Type["Task"]


class Task:
    upstreams: Union[Tuple[TaskClass, ...], TaskClass] = None
    downstreams: Union[Tuple[TaskClass, ...], TaskClass] = None


class Task_:
    @property
    def task_id(self):
        return qualname(self.__class__)

    @property
    def upstream(self) -> Union[Tuple[TaskClass, ...], TaskClass]:
        pass

    @property
    def downstream(self) -> Union[Tuple[TaskClass, ...], TaskClass]:
        pass


@immutable
class TaskPair:
    up: TaskClass
    down: TaskClass


class TaskTree:
    def __init__(self, taskset: Set[Task], taskpairs: Sequence[TaskPair]):

        self._taskset = taskset
        self._taskpairs = taskpairs

        dag = nx.DiGraph()
        dag.add_nodes_from(taskset)
        dag.add_edges_from((pair.up, pair.down) for pair in taskpairs)

        self._dag = dag

    @property
    def dag(self):
        return self._dag

    @property
    def roots(self) -> List[TaskClass]:
        return [node for node in self.dag.nodes() if self.dag.in_degree(node) == 0]

    @property
    def leaves(self) -> List[TaskClass]:
        return [node for node in self.dag.nodes() if self.dag.out_degree(node) == 0]

    @property
    def nodes(self) -> Sequence[TaskClass]:
        return self.dag.nodes

    @property
    def edges(self) -> Sequence[Tuple[TaskClass, TaskClass]]:
        return self.dag.edges


def collect_taskset(
    module: ModuleType, taskclass: TaskClass = Task
) -> Generator[TaskClass, None, None]:

    for cls in collect_objects(
        module,
        predicate=lambda obj: isinstance(obj, type) and issubclass(obj, Task),
    ):

        yield cls  # return task class with no duplication


def build_taskpairs(
    taskset: Set[TaskClass], taskclass: TaskClass = Task
) -> Generator[TaskPair, None, None]:

    cached = set()

    for cls in taskset:

        ups = cls.upstreams  # could be None, Task or Tuple[Task, ...]

        if isinstance(ups, type) and issubclass(ups, taskclass):
            ups = [ups]

        for u in ups or []:

            pair = TaskPair(up=u, down=cls)

            if pair not in cached:

                cached.add(pair)

                yield pair

        downs = cls.downstreams  # could be None, Task or Tuple[Task, ...]

        if isinstance(downs, type) and issubclass(downs, taskclass):
            downs = [downs]

        for d in downs or []:

            pair = TaskPair(up=cls, down=d)

            if pair not in cached:

                cached.add(pair)

                yield pair
