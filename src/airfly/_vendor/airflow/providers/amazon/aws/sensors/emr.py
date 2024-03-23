# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class EmrBaseSensor(BaseSensorOperator):
    aws_conn_id: "str | None"


class EmrServerlessJobSensor(BaseSensorOperator):
    application_id: "str"
    job_run_id: "str"
    target_states: "set | frozenset"
    aws_conn_id: "str | None"


class EmrServerlessApplicationSensor(BaseSensorOperator):
    application_id: "str"
    target_states: "set | frozenset"
    aws_conn_id: "str | None"


class EmrContainerSensor(BaseSensorOperator):
    virtual_cluster_id: "str"
    job_id: "str"
    max_retries: "int | None"
    aws_conn_id: "str | None"
    poll_interval: "int"
    deferrable: "bool"


class EmrNotebookExecutionSensor(EmrBaseSensor):
    notebook_execution_id: "str"
    target_states: "Iterable[str] | None"
    failed_states: "Iterable[str] | None"


class EmrJobFlowSensor(EmrBaseSensor):
    job_flow_id: "str"
    target_states: "Iterable[str] | None"
    failed_states: "Iterable[str] | None"
    max_attempts: "int"
    deferrable: "bool"


class EmrStepSensor(EmrBaseSensor):
    job_flow_id: "str"
    step_id: "str"
    target_states: "Iterable[str] | None"
    failed_states: "Iterable[str] | None"
    max_attempts: "int"
    deferrable: "bool"