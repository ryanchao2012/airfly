# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class LocalFilesystemToS3Operator(BaseOperator):
    filename: "str"
    dest_key: "str"
    dest_bucket: "str | None"
    aws_conn_id: "str | None"
    verify: "str | bool | None"
    replace: "bool"
    encrypt: "bool"
    gzip: "bool"
    acl_policy: "str | None"