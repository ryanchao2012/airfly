# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class SageMakerBaseSensor(BaseSensorOperator):
    aws_conn_id: "str"