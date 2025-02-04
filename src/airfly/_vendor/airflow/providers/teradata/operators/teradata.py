# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
)


class TeradataOperator(SQLExecuteQueryOperator):
    teradata_conn_id: "str"
    schema: "str | None"


class TeradataStoredProcedureOperator(BaseOperator):
    procedure: "str"
    teradata_conn_id: "str"
    parameters: "dict | list | None"
