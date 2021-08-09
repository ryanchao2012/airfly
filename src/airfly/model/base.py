from typing import Tuple, Type, Union

from airfly.utils import qualname

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
