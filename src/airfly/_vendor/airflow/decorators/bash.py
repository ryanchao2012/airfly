# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.decorators.base import DecoratedOperator
from airfly._vendor.airflow.operators.bash import BashOperator


class _BashDecoratedOperator(DecoratedOperator, BashOperator):
    python_callable: "Callable"
    op_args: "Collection[Any] | None"
    op_kwargs: "Mapping[str, Any] | None"
