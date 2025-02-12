# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class CloudDataTransferServiceCreateJobOperator(GoogleCloudBaseOperator):
    body: "dict"
    aws_conn_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    project_id: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceUpdateJobOperator(GoogleCloudBaseOperator):
    job_name: "str"
    body: "dict"
    aws_conn_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    project_id: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceDeleteJobOperator(GoogleCloudBaseOperator):
    job_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    project_id: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceRunJobOperator(GoogleCloudBaseOperator):
    job_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    project_id: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceGetOperationOperator(GoogleCloudBaseOperator):
    project_id: "str"
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceListOperationsOperator(GoogleCloudBaseOperator):
    request_filter: "dict"
    project_id: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServicePauseOperationOperator(GoogleCloudBaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceResumeOperationOperator(GoogleCloudBaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceCancelOperationOperator(GoogleCloudBaseOperator):
    operation_name: "str"
    gcp_conn_id: "str"
    api_version: "str"
    google_impersonation_chain: "str | Sequence[str] | None"


class CloudDataTransferServiceS3ToGCSOperator(GoogleCloudBaseOperator):
    s3_bucket: "str"
    gcs_bucket: "str"
    s3_path: "str | None"
    gcs_path: "str | None"
    project_id: "str"
    aws_conn_id: "str | None"
    gcp_conn_id: "str"
    description: "str | None"
    schedule: "dict | None"
    object_conditions: "dict | None"
    transfer_options: "dict | None"
    wait: "bool"
    timeout: "float | None"
    google_impersonation_chain: "str | Sequence[str] | None"
    delete_job_after_completion: "bool"
    aws_role_arn: "str | None"


class CloudDataTransferServiceGCSToGCSOperator(GoogleCloudBaseOperator):
    source_bucket: "str"
    destination_bucket: "str"
    source_path: "str | None"
    destination_path: "str | None"
    project_id: "str"
    gcp_conn_id: "str"
    description: "str | None"
    schedule: "dict | None"
    object_conditions: "dict | None"
    transfer_options: "dict | None"
    wait: "bool"
    timeout: "float | None"
    google_impersonation_chain: "str | Sequence[str] | None"
    delete_job_after_completion: "bool"
