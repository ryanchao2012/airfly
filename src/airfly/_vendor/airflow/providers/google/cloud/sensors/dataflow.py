# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class DataflowJobStatusSensor(BaseSensorOperator):
    job_id: "str"
    expected_statuses: "set[str] | str"
    project_id: "str"
    location: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "int"


class DataflowJobMetricsSensor(BaseSensorOperator):
    job_id: "str"
    callback: "Callable | None"
    fail_on_terminal_state: "bool"
    project_id: "str"
    location: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "int"


class DataflowJobMessagesSensor(BaseSensorOperator):
    job_id: "str"
    callback: "Callable | None"
    fail_on_terminal_state: "bool"
    project_id: "str"
    location: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "int"


class DataflowJobAutoScalingEventsSensor(BaseSensorOperator):
    job_id: "str"
    callback: "Callable | None"
    fail_on_terminal_state: "bool"
    project_id: "str"
    location: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "int"
