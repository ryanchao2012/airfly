# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class SQSSensor(BaseSensorOperator):
    sqs_queue: "_empty"
    aws_conn_id: "str"
    max_messages: "int"
    wait_time_seconds: "int"
