from types import FunctionType
from typing import Dict, Optional, Type, Union

from airfly._ast import Assign, Call, Constant, Name, keyword, stmt
from airfly._vendor import collect_airflow_operators
from airfly.utils import qualname

from .base import Task

available_operators = collect_airflow_operators()


class AirflowTask(Task):

    operator_class: Union[Type, str] = None
    params: Dict[str, Union[FunctionType, str]] = None

    @classmethod
    def resolve_operator(cls) -> Optional[Type]:

        op = cls.operator_class

        if isinstance(op, str):
            basename = op

        elif isinstance(op, type):
            basename = qualname(op, level=1)

        else:
            return

        items = available_operators[basename]

        if len(items) > 1:
            raise ValueError()

        return items[0]

    @classmethod
    def get_dependencies(cls):  # TODO
        pass

    @classmethod
    def get_stmt(cls) -> Optional[stmt]:

        op = cls.resolve_operator()
        if not op:
            return

        op_name = qualname(op)

        _, op_basename = op_name.rsplit(".", 1)

        task_id = qualname(cls)
        task_varname = task_id.replace(".", "_")

        avai_params = {}
        for base in op.mro()[::-1]:
            avai_params.update(getattr(base, "__annotations__", {}))

        params = dict(task_id=task_id)

        for k, v in (cls.params or {}).items():
            if k in avai_params:
                params.update({k: v})

        assign = Assign(
            targets=[Name(id=task_varname)],
            value=Call(
                func=Name(id=op_basename),
                keywords=[
                    keyword(
                        arg=k,
                        value=(
                            Name(id=qualname(v, level=1))
                            if isinstance(v, FunctionType)
                            else Constant(value=v)  # TODO: handle callable and lambda
                        ),
                    )
                    for k, v in params.items()
                ],
            ),
        )

        return assign

    @classmethod
    def render(cls) -> str:

        _stmt = cls.get_stmt()

        return _stmt.render() if _stmt else ""


class AirflowTask_(Task):
    @property
    def default_params(self):
        return {}

    @property
    def operator_class(self) -> Union[Type, str]:
        raise NotImplementedError

    @property
    def params(self) -> Dict[str, Union[FunctionType, str]]:
        return {}

    @staticmethod
    def resolve_operator(op: Union[Type, str]) -> Type:

        if isinstance(op, str):
            basename = op

        elif isinstance(op, type):
            basename = qualname(op, level=1)

        else:
            raise TypeError(f"got {op}")

        items = available_operators[basename]

        if len(items) > 1:
            raise ValueError()

        return items[0]

    @property
    def dependencies(self):
        pass

    @property
    def _stmt(self) -> stmt:
        op = self.resolve_operator(self.operator_class)
        op_name = qualname(op)
        _, op_basename = op_name.rsplit(".", 1)

        task_id = self.task_id
        task_varname = task_id.replace(".", "_")

        avai_params = {}
        for base in op.mro()[::-1]:
            avai_params.update(getattr(base, "__annotations__", {}))

        params = dict(task_id=task_id)

        for k, v in self.params.items():
            if k in avai_params:
                # if isinstance(
                #     v, (str, FunctionType)
                # ):  # TODO: handle callable and lambda
                params.update({k: v})

        assign = Assign(
            targets=[Name(id=task_varname)],
            value=Call(
                func=Name(id=op_basename),
                keywords=[
                    keyword(
                        arg=k,
                        value=(
                            Name(id=qualname(v, level=1))
                            if isinstance(v, FunctionType)
                            else Constant(value=v)
                        ),
                    )
                    for k, v in params.items()
                ],
            ),
        )

        return assign

    def render(self) -> str:

        return self._stmt.render()
