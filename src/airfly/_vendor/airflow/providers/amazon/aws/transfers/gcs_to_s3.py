# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GCSToS3Operator(BaseOperator):
    gcs_bucket: "str | None"
    bucket: "str | None"
    prefix: "str | None"
    delimiter: "str | None"
    gcp_conn_id: "str"
    dest_aws_conn_id: "str | None"
    dest_s3_key: "str"
    dest_verify: "str | bool | None"
    replace: "bool"
    google_impersonation_chain: "str | Sequence[str] | None"
    dest_s3_extra_args: "dict | None"
    s3_acl_policy: "str | None"
    keep_directory_structure: "bool"
    match_glob: "str | None"
    gcp_user_project: "str | None"
