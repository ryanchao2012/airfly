# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class LocalFilesystemToGoogleDriveOperator(BaseOperator):
    local_paths: "Sequence[Path] | Sequence[str]"
    drive_folder: "Path | str"
    gcp_conn_id: "str"
    delete: "bool"
    ignore_if_missing: "bool"
    chunk_size: "int"
    resumable: "bool"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    folder_id: "str"
    show_full_target_path: "bool"
