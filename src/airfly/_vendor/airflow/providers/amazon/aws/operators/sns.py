# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.base_aws import (
    AwsBaseOperator,
)


class SnsPublishOperator(AwsBaseOperator):
    target_arn: "str"
    message: "str"
    subject: "str | None"
    message_attributes: "dict | None"
