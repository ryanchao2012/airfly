# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class NamedHivePartitionSensor(BaseSensorOperator):
    partition_names: "typing.List[str]"
    metastore_conn_id: "str"
    poke_interval: "int"
    hook: "typing.Any"
