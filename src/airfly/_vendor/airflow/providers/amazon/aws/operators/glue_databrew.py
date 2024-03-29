# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GlueDataBrewStartJobOperator(BaseOperator):
    job_name: "str"
    wait_for_completion: "bool"
    delay: "int"
    deferrable: "bool"
    aws_conn_id: "str | None"
