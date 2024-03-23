# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.operators.branch import BaseBranchOperator


class BranchDateTimeOperator(BaseBranchOperator):
    follow_task_ids_if_true: "str | Iterable[str]"
    follow_task_ids_if_false: "str | Iterable[str]"
    target_lower: "datetime.datetime | datetime.time | None"
    target_upper: "datetime.datetime | datetime.time | None"
    use_task_logical_date: "bool"
    use_task_execution_date: "bool"
