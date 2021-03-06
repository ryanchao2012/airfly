# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class AwsGlueCatalogPartitionSensor(BaseSensorOperator):
    table_name: "str"
    expression: "str"
    aws_conn_id: "str"
    region_name: "typing.Union[str, NoneType]"
    database_name: "str"
    poke_interval: "int"
