# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SFTPToGCSOperator(BaseOperator):
    source_path: "str"
    destination_bucket: "str"
    destination_path: "str | None"
    gcp_conn_id: "str"
    sftp_conn_id: "str"
    mime_type: "str"
    gzip: "bool"
    move_object: "bool"
    impersonation_chain: "str | Sequence[str] | None"
    sftp_prefetch: "bool"
