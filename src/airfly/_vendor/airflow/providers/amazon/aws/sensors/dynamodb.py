# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.sensors.base_aws import AwsBaseSensor


class DynamoDBValueSensor(AwsBaseSensor):
    table_name: "str"
    partition_key_name: "str"
    partition_key_value: "str"
    attribute_name: "str"
    attribute_value: "str | Iterable[str]"
    sort_key_name: "str | None"
    sort_key_value: "str | None"