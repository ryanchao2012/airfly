# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class CassandraRecordSensor(BaseSensorOperator):
    table: "str"
    keys: "typing.Dict[str, str]"
    cassandra_conn_id: "str"