# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.sensors.base_aws import AwsBaseSensor


class AthenaSensor(AwsBaseSensor):
    query_execution_id: "str"
    max_retries: "int | None"
    sleep_time: "int"
