# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class AQLSensor(BaseSensorOperator):
    query: "str"
    arangodb_conn_id: "str"
