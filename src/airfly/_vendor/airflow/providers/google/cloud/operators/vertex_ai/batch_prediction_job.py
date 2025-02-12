# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class CreateBatchPredictionJobOperator(GoogleCloudBaseOperator):
    region: "str"
    project_id: "str"
    job_display_name: "str"
    model_name: "str | Model"
    instances_format: "str"
    predictions_format: "str"
    gcs_source: "str | Sequence[str] | None"
    bigquery_source: "str | None"
    gcs_destination_prefix: "str | None"
    bigquery_destination_prefix: "str | None"
    model_parameters: "dict | None"
    machine_type: "str | None"
    accelerator_type: "str | None"
    accelerator_count: "int | None"
    starting_replica_count: "int | None"
    max_replica_count: "int | None"
    generate_explanation: "bool | None"
    explanation_metadata: "explain.ExplanationMetadata | None"
    explanation_parameters: "explain.ExplanationParameters | None"
    labels: "dict[str, str] | None"
    encryption_spec_key_name: "str | None"
    sync: "bool"
    create_request_timeout: "float | None"
    batch_size: "int | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "int"


class DeleteBatchPredictionJobOperator(GoogleCloudBaseOperator):
    region: "str"
    project_id: "str"
    batch_prediction_job_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GetBatchPredictionJobOperator(GoogleCloudBaseOperator):
    region: "str"
    project_id: "str"
    batch_prediction_job: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class ListBatchPredictionJobsOperator(GoogleCloudBaseOperator):
    region: "str"
    project_id: "str"
    filter: "str | None"
    page_size: "int | None"
    page_token: "str | None"
    read_mask: "str | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
