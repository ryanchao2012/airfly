# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.operators.sql import SQLCheckOperator


class DruidCheckOperator(SQLCheckOperator):
    druid_broker_conn_id: "str"
