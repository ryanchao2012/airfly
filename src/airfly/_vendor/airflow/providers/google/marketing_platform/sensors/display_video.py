# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class GoogleDisplayVideo360GetSDFDownloadOperationSensor(BaseSensorOperator):
    operation_name: "str"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    mode: "str"
    poke_interval: "int"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360RunQuerySensor(BaseSensorOperator):
    query_id: "str"
    report_id: "str"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
