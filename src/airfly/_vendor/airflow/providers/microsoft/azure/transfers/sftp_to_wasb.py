# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SFTPToWasbOperator(BaseOperator):
    sftp_source_path: "str"
    container_name: "str"
    blob_prefix: "str"
    sftp_conn_id: "str"
    wasb_conn_id: "str"
    load_options: "dict | None"
    move_object: "bool"
    wasb_overwrite_object: "bool"
    create_container: "bool"
