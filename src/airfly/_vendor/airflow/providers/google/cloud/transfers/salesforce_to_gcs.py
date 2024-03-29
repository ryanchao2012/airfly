# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SalesforceToGcsOperator(BaseOperator):
    query: "str"
    bucket_name: "str"
    object_name: "str"
    salesforce_conn_id: "str"
    include_deleted: "bool"
    query_params: "dict | None"
    export_format: "str"
    coerce_to_timestamp: "bool"
    record_time_added: "bool"
    gzip: "bool"
    gcp_conn_id: "str"
