import pkgutil
from importlib._bootstrap_external import SourceFileLoader
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    List,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import attr
import networkx as nx

from .utils import qualname

T = TypeVar("T")

TaskClass = Type["Task"]


class Task:
    @property
    def upstream(self) -> Union[Tuple[TaskClass, ...], TaskClass]:
        pass

    @property
    def downstream(self) -> Union[Tuple[TaskClass, ...], TaskClass]:
        pass


class AirflowTask(Task):
    @property
    def operator_class(self) -> str:
        raise NotImplementedError

    @property
    def kargs(self) -> Dict[str, Any]:
        return {}


def make_task(obj: T, upstream: Union[Callable, TaskClass]) -> T:
    pass


def is_taskclass(obj) -> bool:
    return isinstance(obj, type) and issubclass(obj, Task)


def equipped_airfly(obj) -> bool:

    return isinstance(obj, Callable) and hasattr(obj, "__airfly_task__")


def collect_taskclass_from_module(modname: str, exclude: str = None) -> List[TaskClass]:

    tasks = set()
    loader: SourceFileLoader = pkgutil.get_loader(modname)
    module = loader.load_module(modname)

    for finder, name, ispkg in pkgutil.walk_packages(
        module.__path__, module.__name__ + "."
    ):

        mod = finder.find_module(name).load_module(name)

        for name, obj in mod.__dict__.items():

            if is_taskclass(obj) and obj.__module__.startswith(modname):
                tasks.add(obj)
            elif equipped_airfly(obj) and obj.__module__.startswith(modname):
                tasks.add(obj.__airfly_task__)

    sorted_tasks = sorted(tasks, key=lambda t: qualname(t))

    return sorted_tasks


@attr.s(slots=True, auto_attribs=True, frozen=True)
class TaskPair:
    this: TaskClass
    upstream: TaskClass


class TaskTree:
    def __init__(self, taskset: Set[TaskClass]):

        self._taskset = taskset
        g = nx.DiGraph()

        taskpairs = list(set(self.pairs(taskset, field="upstream")))
        sorted_taskpairs = sorted(
            taskpairs,
            key=lambda pair: qualname(pair.upstream) + "-" + qualname(pair.task),
        )

        g.add_nodes_from(taskset)
        g.add_edges_from((pair.upstream, pair.task) for pair in sorted_taskpairs)

        self._g = g

    @classmethod
    def traverse(cls, taskset: Set[TaskClass]) -> Iterable[TaskClass]:
        for taskclass in taskset:
            if not is_taskclass(taskclass):
                continue

            yield taskclass

    @classmethod
    def pairs(
        cls, taskset: Set[TaskClass], field: str = "upstream"
    ) -> Generator[TaskPair, None, None]:

        for taskclass in taskset:
            if not is_taskclass(taskclass):
                continue

            upstream = getattr(taskclass(), field, None)

            if is_taskclass(upstream) and (upstream in taskset):
                yield TaskPair(this=taskclass, upstream=upstream)

            elif isinstance(upstream, Iterable):
                for up in upstream:
                    if is_taskclass(up) and (up in taskset):
                        yield TaskPair(this=taskclass, upstream=up)

    @property
    def roots(self):
        return [node for node in self._g.nodes() if self._g.in_degree(node) == 0]

    @property
    def leaves(self):
        return [node for node in self._g.nodes() if self._g.out_degree(node) == 0]

    @property
    def nodes(self):
        return self._g.nodes

    @property
    def edges(self):
        return self._g.edges
