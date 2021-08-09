# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GoogleApiToS3Operator(BaseOperator):
    google_api_service_name: "str"
    google_api_service_version: "str"
    google_api_endpoint_path: "str"
    google_api_endpoint_params: "dict"
    s3_destination_key: "str"
    google_api_response_via_xcom: "typing.Union[str, NoneType]"
    google_api_endpoint_params_via_xcom: "typing.Union[str, NoneType]"
    google_api_endpoint_params_via_xcom_task_ids: "typing.Union[str, NoneType]"
    google_api_pagination: "bool"
    google_api_num_retries: "int"
    s3_overwrite: "bool"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    aws_conn_id: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
