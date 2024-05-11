from typing import Any, Dict, Iterable, Type, Union

TaskClass = Type["MyTask"]


class MyTask:
    # provide these attributes
    op_class: str = "BashOperator"
    op_params: Dict[str, Any] = None
    op_module: str = None
    upstream: Union[TaskClass, Iterable[TaskClass]] = None
    downstream: Union[TaskClass, Iterable[TaskClass]] = None

    # other stuff
