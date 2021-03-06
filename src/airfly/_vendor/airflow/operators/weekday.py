# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.operators.branch import BaseBranchOperator


class BranchDayOfWeekOperator(BaseBranchOperator):
    follow_task_ids_if_true: "typing.Union[str, typing.Iterable[str]]"
    follow_task_ids_if_false: "typing.Union[str, typing.Iterable[str]]"
    week_day: "typing.Union[str, typing.Iterable[str]]"
    use_task_execution_day: "bool"
