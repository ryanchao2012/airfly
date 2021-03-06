# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class FileToWasbOperator(BaseOperator):
    file_path: "str"
    container_name: "str"
    blob_name: "str"
    wasb_conn_id: "str"
    load_options: "typing.Union[dict, NoneType]"
