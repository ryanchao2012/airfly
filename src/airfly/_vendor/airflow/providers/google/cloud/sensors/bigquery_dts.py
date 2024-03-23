# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class BigQueryDataTransferServiceTransferRunSensor(BaseSensorOperator):
    run_id: "str"
    transfer_config_id: "str"
    expected_statuses: "set[str | TransferState | int] | str | TransferState | int"
    project_id: "str | None"
    gcp_conn_id: "str"
    retry: "Retry | _MethodDefault"
    request_timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
