# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DruidOperator(BaseOperator):
    json_index_file: "str"
    druid_ingest_conn_id: "str"
    timeout: "int"
    max_ingestion_time: "int | None"
    ingestion_type: "IngestionType"
    verify_ssl: "bool"
