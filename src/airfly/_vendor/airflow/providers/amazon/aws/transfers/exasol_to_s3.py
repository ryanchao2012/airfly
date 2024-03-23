# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class ExasolToS3Operator(BaseOperator):
    query_or_table: "str"
    key: "str"
    bucket_name: "str | None"
    replace: "bool"
    encrypt: "bool"
    gzip: "bool"
    acl_policy: "str | None"
    query_params: "dict | None"
    export_params: "dict | None"
    exasol_conn_id: "str"
    aws_conn_id: "str | None"
