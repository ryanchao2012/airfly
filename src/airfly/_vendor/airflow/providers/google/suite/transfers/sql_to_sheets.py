# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.common.sql.operators.sql import BaseSQLOperator


class SQLToGoogleSheetsOperator(BaseSQLOperator):
    sql: "str"
    spreadsheet_id: "str"
    sql_conn_id: "str"
    parameters: "Iterable | Mapping[str, Any] | None"
    database: "str | None"
    spreadsheet_range: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
