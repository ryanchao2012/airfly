# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class ComputeEngineBaseOperator(GoogleCloudBaseOperator):
    zone: "str"
    resource_id: "str | None"
    project_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineInsertInstanceOperator(ComputeEngineBaseOperator):
    body: "dict"
    zone: "str"
    resource_id: "str | None"
    project_id: "str | None"
    request_id: "str | None"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineInsertInstanceFromTemplateOperator(ComputeEngineBaseOperator):
    source_instance_template: "str"
    body: "dict"
    zone: "str"
    resource_id: "str | None"
    project_id: "str | None"
    request_id: "str | None"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineDeleteInstanceOperator(ComputeEngineBaseOperator):
    resource_id: "str"
    zone: "str"
    request_id: "str | None"
    project_id: "str | None"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineStartInstanceOperator(ComputeEngineBaseOperator):
    zone: "str"
    resource_id: "str | None"
    project_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineStopInstanceOperator(ComputeEngineBaseOperator):
    zone: "str"
    resource_id: "str | None"
    project_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineSetMachineTypeOperator(ComputeEngineBaseOperator):
    zone: "str"
    resource_id: "str"
    body: "dict"
    project_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineInsertInstanceTemplateOperator(ComputeEngineBaseOperator):
    body: "dict"
    project_id: "str | None"
    resource_id: "str | None"
    request_id: "str | None"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineDeleteInstanceTemplateOperator(ComputeEngineBaseOperator):
    resource_id: "str"
    request_id: "str | None"
    project_id: "str | None"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineCopyInstanceTemplateOperator(ComputeEngineBaseOperator):
    resource_id: "str"
    body_patch: "dict"
    project_id: "str | None"
    request_id: "str | None"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineInstanceGroupUpdateManagerTemplateOperator(
    ComputeEngineBaseOperator
):
    resource_id: "str"
    zone: "str"
    source_template: "str"
    destination_template: "str"
    project_id: "str | None"
    update_policy: "dict[str, Any] | None"
    request_id: "str | None"
    gcp_conn_id: "str"
    api_version: "_empty"
    impersonation_chain: "str | Sequence[str] | None"


class ComputeEngineInsertInstanceGroupManagerOperator(ComputeEngineBaseOperator):
    body: "dict"
    zone: "str"
    project_id: "str | None"
    resource_id: "str | None"
    request_id: "str | None"
    gcp_conn_id: "str"
    api_version: "_empty"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    impersonation_chain: "str | Sequence[str] | None"
    validate_body: "bool"


class ComputeEngineDeleteInstanceGroupManagerOperator(ComputeEngineBaseOperator):
    resource_id: "str"
    zone: "str"
    project_id: "str | None"
    request_id: "str | None"
    gcp_conn_id: "str"
    api_version: "_empty"
    retry: "Retry | None"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    impersonation_chain: "str | Sequence[str] | None"
    validate_body: "bool"
