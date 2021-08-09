# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudFunctionDeleteFunctionOperator(BaseOperator):
    name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudFunctionDeployFunctionOperator(BaseOperator):
    location: "str"
    body: "typing.Dict"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    zip_path: "typing.Union[str, NoneType]"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
