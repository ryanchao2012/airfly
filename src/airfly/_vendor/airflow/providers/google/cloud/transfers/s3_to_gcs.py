# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.s3 import S3ListOperator


class S3ToGCSOperator(S3ListOperator):
    bucket: "_empty"
    prefix: "_empty"
    apply_gcs_prefix: "_empty"
    delimiter: "_empty"
    aws_conn_id: "_empty"
    verify: "_empty"
    gcp_conn_id: "_empty"
    dest_gcs: "_empty"
    replace: "_empty"
    gzip: "_empty"
    google_impersonation_chain: "str | Sequence[str] | None"
    deferrable: "_empty"
    poll_interval: "int"
