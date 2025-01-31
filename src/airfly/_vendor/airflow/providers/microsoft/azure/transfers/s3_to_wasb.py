# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class S3ToAzureBlobStorageOperator(BaseOperator):
    aws_conn_id: "str"
    wasb_conn_id: "str"
    s3_bucket: "str"
    container_name: "str"
    s3_prefix: "str | None"
    s3_key: "str | None"
    blob_prefix: "str | None"
    blob_name: "str | None"
    create_container: "bool"
    replace: "bool"
    s3_verify: "bool"
    s3_extra_args: "dict | None"
    wasb_extra_args: "dict | None"
