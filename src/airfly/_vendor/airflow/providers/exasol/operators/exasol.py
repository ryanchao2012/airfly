# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
)


class ExasolOperator(SQLExecuteQueryOperator):
    exasol_conn_id: "str"
    schema: "str | None"
    handler: "_empty"
