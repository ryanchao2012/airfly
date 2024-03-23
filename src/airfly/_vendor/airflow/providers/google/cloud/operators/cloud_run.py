# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class CloudRunCreateJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    job: "dict | Job"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudRunUpdateJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    job: "dict | Job"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudRunDeleteJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudRunListJobsOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    show_deleted: "bool"
    limit: "int | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudRunExecuteJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    overrides: "dict[str, Any] | None"
    polling_period_seconds: "float"
    timeout_seconds: "float | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
