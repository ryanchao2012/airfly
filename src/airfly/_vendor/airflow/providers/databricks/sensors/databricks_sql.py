# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class DatabricksSqlSensor(BaseSensorOperator):
    databricks_conn_id: "str"
    http_path: "str | None"
    sql_warehouse_name: "str | None"
    session_configuration: "_empty"
    http_headers: "list[tuple[str, str]] | None"
    catalog: "str"
    schema: "str"
    sql: "str | Iterable[str]"
    handler: "Callable[[Any], Any]"
    client_parameters: "dict[str, Any] | None"
