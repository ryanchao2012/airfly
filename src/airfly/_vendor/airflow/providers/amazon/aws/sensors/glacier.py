# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.sensors.base_aws import AwsBaseSensor


class GlacierJobOperationSensor(AwsBaseSensor):
    vault_name: "str"
    job_id: "str"
    poke_interval: "int"
    mode: "str"
