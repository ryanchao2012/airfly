# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudDataTransferServiceCancelOperationOperator(BaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceCreateJobOperator(BaseOperator):
    body: "dict"
    aws_conn_id: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceDeleteJobOperator(BaseOperator):
    job_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    project_id: "typing.Union[str, NoneType]"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceGCSToGCSOperator(BaseOperator):
    source_bucket: "str"
    destination_bucket: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    description: "typing.Union[str, NoneType]"
    schedule: "typing.Union[typing.Dict, NoneType]"
    object_conditions: "typing.Union[typing.Dict, NoneType]"
    transfer_options: "typing.Union[typing.Dict, NoneType]"
    wait: "bool"
    timeout: "typing.Union[float, NoneType]"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
    delete_job_after_completion: "bool"


class CloudDataTransferServiceGetOperationOperator(BaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceListOperationsOperator(BaseOperator):
    request_filter: "typing.Union[typing.Dict, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServicePauseOperationOperator(BaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceResumeOperationOperator(BaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDataTransferServiceS3ToGCSOperator(BaseOperator):
    s3_bucket: "str"
    gcs_bucket: "str"
    project_id: "typing.Union[str, NoneType]"
    aws_conn_id: "str"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    description: "typing.Union[str, NoneType]"
    schedule: "typing.Union[typing.Dict, NoneType]"
    object_conditions: "typing.Union[typing.Dict, NoneType]"
    transfer_options: "typing.Union[typing.Dict, NoneType]"
    wait: "bool"
    timeout: "typing.Union[float, NoneType]"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
    delete_job_after_completion: "bool"


class CloudDataTransferServiceUpdateJobOperator(BaseOperator):
    job_name: "str"
    body: "dict"
    aws_conn_id: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
