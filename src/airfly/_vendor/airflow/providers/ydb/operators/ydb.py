# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
)


class YDBExecuteQueryOperator(SQLExecuteQueryOperator):
    sql: "str | list[str]"
    is_ddl: "bool"
    ydb_conn_id: "str"
    parameters: "Mapping | Iterable | None"
