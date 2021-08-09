# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class PrestoToMySqlOperator(BaseOperator):
    sql: "str"
    mysql_table: "str"
    presto_conn_id: "str"
    mysql_conn_id: "str"
    mysql_preoperator: "typing.Union[str, NoneType]"
