# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class DatabricksPartitionSensor(BaseSensorOperator):
    databricks_conn_id: "str"
    http_path: "str | None"
    sql_warehouse_name: "str | None"
    session_configuration: "_empty"
    http_headers: "list[tuple[str, str]] | None"
    catalog: "str"
    schema: "str"
    table_name: "str"
    partitions: "dict"
    partition_operator: "str"
    handler: "Callable[[Any], Any]"
    client_parameters: "dict[str, Any] | None"
