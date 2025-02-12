# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SageMakerBaseOperator(BaseOperator):
    config: "dict"
    aws_conn_id: "str | None"


class SageMakerProcessingOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"
    wait_for_completion: "bool"
    print_log: "bool"
    check_interval: "int"
    max_attempts: "int | None"
    max_ingestion_time: "int | None"
    action_if_job_exists: "str"
    deferrable: "bool"


class SageMakerEndpointConfigOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"


class SageMakerEndpointOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"
    wait_for_completion: "bool"
    check_interval: "int"
    max_ingestion_time: "int | None"
    operation: "str"
    deferrable: "bool"


class SageMakerTransformOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"
    wait_for_completion: "bool"
    check_interval: "int"
    max_attempts: "int | None"
    max_ingestion_time: "int | None"
    check_if_job_exists: "bool"
    action_if_job_exists: "str"
    check_if_model_exists: "bool"
    action_if_model_exists: "str"
    deferrable: "bool"


class SageMakerTuningOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"
    wait_for_completion: "bool"
    check_interval: "int"
    max_ingestion_time: "int | None"
    deferrable: "bool"


class SageMakerModelOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"


class SageMakerTrainingOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"
    wait_for_completion: "bool"
    print_log: "bool"
    check_interval: "int"
    max_attempts: "int | None"
    max_ingestion_time: "int | None"
    check_if_job_exists: "bool"
    action_if_job_exists: "str"
    deferrable: "bool"


class SageMakerDeleteModelOperator(SageMakerBaseOperator):
    config: "dict"
    aws_conn_id: "str | None"


class SageMakerStartPipelineOperator(SageMakerBaseOperator):
    aws_conn_id: "str | None"
    pipeline_name: "str"
    display_name: "str"
    pipeline_params: "dict | None"
    wait_for_completion: "bool"
    check_interval: "int"
    waiter_max_attempts: "int"
    verbose: "bool"
    deferrable: "bool"


class SageMakerStopPipelineOperator(SageMakerBaseOperator):
    aws_conn_id: "str | None"
    pipeline_exec_arn: "str"
    wait_for_completion: "bool"
    check_interval: "int"
    waiter_max_attempts: "int"
    verbose: "bool"
    fail_if_not_running: "bool"
    deferrable: "bool"


class SageMakerRegisterModelVersionOperator(SageMakerBaseOperator):
    image_uri: "str"
    model_url: "str"
    package_group_name: "str"
    package_group_desc: "str"
    package_desc: "str"
    model_approval: "ApprovalStatus"
    extras: "dict | None"
    aws_conn_id: "str | None"
    config: "dict | None"


class SageMakerAutoMLOperator(SageMakerBaseOperator):
    job_name: "str"
    s3_input: "str"
    target_attribute: "str"
    s3_output: "str"
    role_arn: "str"
    compressed_input: "bool"
    time_limit: "int | None"
    autodeploy_endpoint_name: "str | None"
    extras: "dict | None"
    wait_for_completion: "bool"
    check_interval: "int"
    aws_conn_id: "str | None"
    config: "dict | None"


class SageMakerCreateExperimentOperator(SageMakerBaseOperator):
    name: "str"
    description: "str | None"
    tags: "dict | None"
    aws_conn_id: "str | None"


class SageMakerCreateNotebookOperator(BaseOperator):
    instance_name: "str"
    instance_type: "str"
    role_arn: "str"
    volume_size_in_gb: "int | None"
    volume_kms_key_id: "str | None"
    lifecycle_config_name: "str | None"
    direct_internet_access: "str | None"
    root_access: "str | None"
    create_instance_kwargs: "dict[str, Any] | None"
    wait_for_completion: "bool"
    aws_conn_id: "str | None"


class SageMakerStopNotebookOperator(BaseOperator):
    instance_name: "str"
    wait_for_completion: "bool"
    aws_conn_id: "str | None"


class SageMakerDeleteNotebookOperator(BaseOperator):
    instance_name: "str"
    wait_for_completion: "bool"
    aws_conn_id: "str | None"


class SageMakerStartNoteBookOperator(BaseOperator):
    instance_name: "str"
    wait_for_completion: "bool"
    aws_conn_id: "str | None"
