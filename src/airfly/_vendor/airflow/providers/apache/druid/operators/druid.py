# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DruidOperator(BaseOperator):
    json_index_file: "str"
    druid_ingest_conn_id: "str"
    max_ingestion_time: "typing.Union[int, NoneType]"
