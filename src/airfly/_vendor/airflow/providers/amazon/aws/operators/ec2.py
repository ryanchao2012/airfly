# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class EC2StartInstanceOperator(BaseOperator):
    instance_id: "str"
    aws_conn_id: "str | None"
    region_name: "str | None"
    check_interval: "float"


class EC2StopInstanceOperator(BaseOperator):
    instance_id: "str"
    aws_conn_id: "str | None"
    region_name: "str | None"
    check_interval: "float"


class EC2CreateInstanceOperator(BaseOperator):
    image_id: "str"
    max_count: "int"
    min_count: "int"
    aws_conn_id: "str | None"
    region_name: "str | None"
    poll_interval: "int"
    max_attempts: "int"
    config: "dict | None"
    wait_for_completion: "bool"


class EC2TerminateInstanceOperator(BaseOperator):
    instance_ids: "str | list[str]"
    aws_conn_id: "str | None"
    region_name: "str | None"
    poll_interval: "int"
    max_attempts: "int"
    wait_for_completion: "bool"


class EC2RebootInstanceOperator(BaseOperator):
    instance_ids: "str | list[str]"
    aws_conn_id: "str | None"
    region_name: "str | None"
    poll_interval: "int"
    max_attempts: "int"
    wait_for_completion: "bool"


class EC2HibernateInstanceOperator(BaseOperator):
    instance_ids: "str | list[str]"
    aws_conn_id: "str | None"
    region_name: "str | None"
    poll_interval: "int"
    max_attempts: "int"
    wait_for_completion: "bool"
