# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class LocalFilesystemToGCSOperator(BaseOperator):
    src: "_empty"
    dst: "_empty"
    bucket: "_empty"
    gcp_conn_id: "_empty"
    google_cloud_storage_conn_id: "_empty"
    mime_type: "_empty"
    delegate_to: "_empty"
    gzip: "_empty"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
