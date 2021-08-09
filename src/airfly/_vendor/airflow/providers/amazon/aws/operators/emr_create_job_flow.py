# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class EmrCreateJobFlowOperator(BaseOperator):
    aws_conn_id: "str"
    emr_conn_id: "str"
    job_flow_overrides: "typing.Union[str, typing.Dict[str, typing.Any], NoneType]"
    region_name: "typing.Union[str, NoneType]"
