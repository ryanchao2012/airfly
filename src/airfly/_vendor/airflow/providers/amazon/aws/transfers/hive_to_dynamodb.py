# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class HiveToDynamoDBOperator(BaseOperator):
    sql: "str"
    table_name: "str"
    table_keys: "list"
    pre_process: "typing.Union[typing.Callable, NoneType]"
    pre_process_args: "typing.Union[list, NoneType]"
    pre_process_kwargs: "typing.Union[list, NoneType]"
    region_name: "typing.Union[str, NoneType]"
    schema: "str"
    hiveserver2_conn_id: "str"
    aws_conn_id: "str"
