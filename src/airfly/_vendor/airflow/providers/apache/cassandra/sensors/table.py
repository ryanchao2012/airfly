# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class CassandraTableSensor(BaseSensorOperator):
    table: "str"
    cassandra_conn_id: "str"
