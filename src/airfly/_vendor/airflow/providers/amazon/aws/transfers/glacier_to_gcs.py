# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GlacierToGCSOperator(BaseOperator):
    aws_conn_id: "str | None"
    gcp_conn_id: "str"
    vault_name: "str"
    bucket_name: "str"
    object_name: "str"
    gzip: "bool"
    chunk_size: "int"
    google_impersonation_chain: "str | Sequence[str] | None"