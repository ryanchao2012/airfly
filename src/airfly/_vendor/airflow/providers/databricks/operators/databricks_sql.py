# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
)


class DatabricksSqlOperator(SQLExecuteQueryOperator):
    databricks_conn_id: "str"
    http_path: "str | None"
    sql_endpoint_name: "str | None"
    session_configuration: "_empty"
    http_headers: "list[tuple[str, str]] | None"
    catalog: "str | None"
    schema: "str | None"
    output_path: "str | None"
    output_format: "str"
    csv_params: "dict[str, Any] | None"
    client_parameters: "dict[str, Any] | None"


class DatabricksCopyIntoOperator(BaseOperator):
    table_name: "str"
    file_location: "str"
    file_format: "str"
    databricks_conn_id: "str"
    http_path: "str | None"
    sql_endpoint_name: "str | None"
    session_configuration: "_empty"
    http_headers: "list[tuple[str, str]] | None"
    client_parameters: "dict[str, Any] | None"
    catalog: "str | None"
    schema: "str | None"
    files: "list[str] | None"
    pattern: "str | None"
    expression_list: "str | None"
    credential: "dict[str, str] | None"
    storage_credential: "str | None"
    encryption: "dict[str, str] | None"
    format_options: "dict[str, str] | None"
    force_copy: "bool | None"
    copy_options: "dict[str, str] | None"
    validate: "bool | int | None"
