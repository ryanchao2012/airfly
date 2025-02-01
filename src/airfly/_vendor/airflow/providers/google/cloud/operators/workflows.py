# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class WorkflowsCreateWorkflowOperator(GoogleCloudBaseOperator):
    workflow: "dict"
    workflow_id: "str"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    force_rerun: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsUpdateWorkflowOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    location: "str"
    project_id: "str"
    update_mask: "FieldMask | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsDeleteWorkflowOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsListWorkflowsOperator(GoogleCloudBaseOperator):
    location: "str"
    project_id: "str"
    filter_: "str | None"
    order_by: "str | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsGetWorkflowOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsCreateExecutionOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    execution: "dict"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsCancelExecutionOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    execution_id: "str"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsListExecutionsOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    location: "str"
    start_date_filter: "datetime.datetime | None"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class WorkflowsGetExecutionOperator(GoogleCloudBaseOperator):
    workflow_id: "str"
    execution_id: "str"
    location: "str"
    project_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
