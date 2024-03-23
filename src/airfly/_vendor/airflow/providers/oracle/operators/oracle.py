# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
)


class OracleOperator(SQLExecuteQueryOperator):
    pass


class OracleStoredProcedureOperator(BaseOperator):
    procedure: "str"
    oracle_conn_id: "str"
    parameters: "dict | list | None"
