# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DbtCloudRunJobOperator(BaseOperator):
    dbt_cloud_conn_id: "str"
    job_id: "int"
    account_id: "int | None"
    trigger_reason: "str | None"
    steps_override: "list[str] | None"
    schema_override: "str | None"
    wait_for_termination: "bool"
    timeout: "int"
    check_interval: "int"
    additional_run_config: "dict[str, Any] | None"
    reuse_existing_run: "bool"
    retry_from_failure: "bool"
    deferrable: "bool"


class DbtCloudGetJobRunArtifactOperator(BaseOperator):
    dbt_cloud_conn_id: "str"
    run_id: "int"
    path: "str"
    account_id: "int | None"
    step: "int | None"
    output_file_name: "str | None"


class DbtCloudListJobsOperator(BaseOperator):
    dbt_cloud_conn_id: "str"
    account_id: "int | None"
    project_id: "int | None"
    order_by: "str | None"
