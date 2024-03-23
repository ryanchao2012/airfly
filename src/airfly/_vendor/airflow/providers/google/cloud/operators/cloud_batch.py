# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class CloudBatchSubmitJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    job: "dict | Job"
    polling_period_seconds: "float"
    timeout_seconds: "float | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"


class CloudBatchDeleteJobOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    timeout: "float | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudBatchListJobsOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    gcp_conn_id: "str"
    filter: "str | None"
    limit: "int | None"
    impersonation_chain: "str | Sequence[str] | None"


class CloudBatchListTasksOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    job_name: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    group_name: "str"
    filter: "str | None"
    limit: "int | None"
