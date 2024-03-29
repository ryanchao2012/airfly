# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class GlueCatalogPartitionSensor(BaseSensorOperator):
    table_name: "str"
    expression: "str"
    aws_conn_id: "str | None"
    region_name: "str | None"
    database_name: "str"
    poke_interval: "int"
    deferrable: "bool"
