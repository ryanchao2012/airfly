# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.transfers.bigquery_to_sql import (
    BigQueryToSqlBaseOperator,
)


class BigQueryToPostgresOperator(BigQueryToSqlBaseOperator):
    target_table_name: "str"
    postgres_conn_id: "str"