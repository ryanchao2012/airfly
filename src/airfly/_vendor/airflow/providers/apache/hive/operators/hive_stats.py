# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class HiveStatsCollectionOperator(BaseOperator):
    table: "str"
    partition: "typing.Any"
    extra_exprs: "typing.Union[typing.Dict[str, typing.Any], NoneType]"
    excluded_columns: "typing.Union[typing.List[str], NoneType]"
    assignment_func: "typing.Union[typing.Callable[[str, str], typing.Union[typing.Dict[typing.Any, typing.Any], NoneType]], NoneType]"
    metastore_conn_id: "str"
    presto_conn_id: "str"
    mysql_conn_id: "str"
