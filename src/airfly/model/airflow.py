from types import FunctionType
from typing import Dict, List, Optional, Sequence, Set, Type, Union

from airfly._ast import Assign, Call, Constant, ImportFrom, Name, alias, keyword, stmt
from airfly._vendor import collect_airflow_operators
from airfly.utils import qualname

from .base import Task

available_operators = collect_airflow_operators()


class AirflowTask(Task):

    operator_class: Union[Type, str] = None
    params: Dict[str, Union[FunctionType, str]] = None

    @classmethod
    def _resolve_operator(cls) -> Optional[Type]:

        op = cls.operator_class

        if isinstance(op, str):
            basename = op

        elif isinstance(op, type):
            basename = qualname(op, level=1)

        else:
            return

        items = available_operators[basename]

        if len(items) > 1:
            raise ValueError()  # TODO:

        return items[0]

    @classmethod
    def _resolve_dependency_from_params(
        cls, obj: Union[Dict, List] = None
    ) -> List[Union[FunctionType, Type]]:

        deps = []

        if isinstance(obj, type(None)):

            params = cls.params or {}

            deps.extend(cls._resolve_dependency_from_params(params))

        elif isinstance(obj, str):
            return []

        elif isinstance(obj, (Sequence, Set, Dict)):

            iterator = (
                (el for el in obj)
                if isinstance(obj, (Sequence, Set))
                else (v for _, v in obj.items())
            )

            for el in iterator:
                if isinstance(el, (str, type(None))):
                    continue

                elif isinstance(el, (Sequence, Set, Dict)):  # NOTE: list, tuple, set
                    deps.extend(cls._resolve_dependency_from_params(el))

                elif isinstance(el, FunctionType):
                    deps.append(el)

        return list(set(deps))

    @classmethod
    def collect_dep_stmts(cls) -> List[stmt]:
        """Collect all stmts for all dependencies"""

        param_deps = cls._resolve_dependency_from_params()
        op_dev = cls._resolve_operator()

        op_modname, op_basename = qualname(op_dev).rsplit(".", 1)
        op_modname = op_modname.replace("airfly._vendor.", "")

        dep_stmts = [ImportFrom(module=op_modname, names=[alias(name=op_basename)])]

        for dep in param_deps:
            fn_modname, fn_basename = qualname(dep).rsplit(".", 1)
            dep_stmts.append(
                ImportFrom(module=fn_modname, names=[alias(name=fn_basename)])
            )

        return dep_stmts

    @classmethod
    def to_stmt(cls) -> Optional[stmt]:

        op = cls._resolve_operator()
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

    # @classmethod
    # def render(cls) -> str:

    #     _stmt = cls.to_stmt()

    #     return _stmt.render() if _stmt else ""
