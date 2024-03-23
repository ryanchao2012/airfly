# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.base_aws import (
    AwsBaseOperator,
)


class GlacierCreateJobOperator(AwsBaseOperator):
    vault_name: "str"


class GlacierUploadArchiveOperator(AwsBaseOperator):
    vault_name: "str"
    body: "object"
    checksum: "str | None"
    archive_description: "str | None"
    account_id: "str | None"