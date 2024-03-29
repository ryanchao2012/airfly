# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLCheckOperator,
    SQLExecuteQueryOperator,
    SQLIntervalCheckOperator,
    SQLValueCheckOperator,
)


class SnowflakeOperator(SQLExecuteQueryOperator):
    pass


class SnowflakeCheckOperator(SQLCheckOperator):
    sql: "str"
    snowflake_conn_id: "str"
    parameters: "Iterable | Mapping[str, Any] | None"
    autocommit: "bool"
    do_xcom_push: "bool"
    warehouse: "str | None"
    database: "str | None"
    role: "str | None"
    schema: "str | None"
    authenticator: "str | None"
    session_parameters: "dict | None"


class SnowflakeValueCheckOperator(SQLValueCheckOperator):
    sql: "str"
    pass_value: "Any"
    tolerance: "Any"
    snowflake_conn_id: "str"
    parameters: "Iterable | Mapping[str, Any] | None"
    autocommit: "bool"
    do_xcom_push: "bool"
    warehouse: "str | None"
    database: "str | None"
    role: "str | None"
    schema: "str | None"
    authenticator: "str | None"
    session_parameters: "dict | None"


class SnowflakeIntervalCheckOperator(SQLIntervalCheckOperator):
    table: "str"
    metrics_thresholds: "dict"
    date_filter_column: "str"
    days_back: "SupportsAbs[int]"
    snowflake_conn_id: "str"
    parameters: "Iterable | Mapping[str, Any] | None"
    autocommit: "bool"
    do_xcom_push: "bool"
    warehouse: "str | None"
    database: "str | None"
    role: "str | None"
    schema: "str | None"
    authenticator: "str | None"
    session_parameters: "dict | None"


class SnowflakeSqlApiOperator(SQLExecuteQueryOperator):
    snowflake_conn_id: "str"
    warehouse: "str | None"
    database: "str | None"
    role: "str | None"
    schema: "str | None"
    authenticator: "str | None"
    session_parameters: "dict[str, Any] | None"
    poll_interval: "int"
    statement_count: "int"
    token_life_time: "timedelta"
    token_renewal_delta: "timedelta"
    bindings: "dict[str, Any] | None"
    deferrable: "bool"
