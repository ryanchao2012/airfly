# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class TeradataToTeradataOperator(BaseOperator):
    dest_teradata_conn_id: "str"
    destination_table: "str"
    source_teradata_conn_id: "str"
    sql: "str"
    sql_params: "dict | None"
    rows_chunk: "int"
