# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class S3PrefixSensor(BaseSensorOperator):
    bucket_name: "str"
    prefix: "str"
    delimiter: "str"
    aws_conn_id: "str"
    verify: "typing.Union[bool, str, NoneType]"
