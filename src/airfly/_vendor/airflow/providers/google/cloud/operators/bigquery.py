# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.common.sql.operators.sql import (
    SQLCheckOperator,
    SQLColumnCheckOperator,
    SQLIntervalCheckOperator,
    SQLTableCheckOperator,
    SQLValueCheckOperator,
)
from airfly._vendor.airflow.providers.google.cloud.openlineage.mixins import (
    _BigQueryOpenLineageMixin,
)
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class BigQueryCreateEmptyDatasetOperator(GoogleCloudBaseOperator):
    dataset_id: "str | None"
    project_id: "str"
    dataset_reference: "dict | None"
    location: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    if_exists: "str"
    exists_ok: "bool | None"


class BigQueryCreateEmptyTableOperator(GoogleCloudBaseOperator):
    dataset_id: "str"
    table_id: "str"
    table_resource: "dict[str, Any] | None"
    project_id: "str"
    schema_fields: "list | None"
    gcs_schema_object: "str | None"
    time_partitioning: "dict | None"
    gcp_conn_id: "str"
    google_cloud_storage_conn_id: "str"
    labels: "dict | None"
    view: "dict | None"
    materialized_view: "dict | None"
    encryption_configuration: "dict | None"
    location: "str | None"
    cluster_fields: "list[str] | None"
    impersonation_chain: "str | Sequence[str] | None"
    if_exists: "str"
    bigquery_conn_id: "str | None"
    exists_ok: "bool | None"


class BigQueryDeleteDatasetOperator(GoogleCloudBaseOperator):
    dataset_id: "str"
    project_id: "str"
    delete_contents: "bool"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryInsertJobOperator(GoogleCloudBaseOperator, _BigQueryOpenLineageMixin):
    configuration: "dict[str, Any]"
    project_id: "str"
    location: "str | None"
    job_id: "str | None"
    force_rerun: "bool"
    reattach_states: "set[str] | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    cancel_on_kill: "bool"
    result_retry: "Retry"
    result_timeout: "float | None"
    deferrable: "bool"
    poll_interval: "float"


class BigQueryCreateExternalTableOperator(GoogleCloudBaseOperator):
    bucket: "str | None"
    source_objects: "list[str] | None"
    destination_project_dataset_table: "str | None"
    table_resource: "dict[str, Any] | None"
    schema_fields: "list | None"
    schema_object: "str | None"
    gcs_schema_bucket: "str | None"
    source_format: "str | None"
    autodetect: "bool"
    compression: "str | None"
    skip_leading_rows: "int | None"
    field_delimiter: "str | None"
    max_bad_records: "int"
    quote_character: "str | None"
    allow_quoted_newlines: "bool"
    allow_jagged_rows: "bool"
    gcp_conn_id: "str"
    google_cloud_storage_conn_id: "str"
    src_fmt_configs: "dict | None"
    labels: "dict | None"
    encryption_configuration: "dict | None"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    bigquery_conn_id: "str | None"


class _BigQueryDbHookMixin:
    pass


class _BigQueryOperatorsEncryptionConfigurationMixin:
    pass


class BigQueryCheckOperator(
    _BigQueryDbHookMixin,
    SQLCheckOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    sql: "str"
    gcp_conn_id: "str"
    use_legacy_sql: "bool"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    labels: "dict | None"
    encryption_configuration: "dict | None"
    deferrable: "bool"
    poll_interval: "float"
    query_params: "list | None"


class BigQueryValueCheckOperator(
    _BigQueryDbHookMixin,
    SQLValueCheckOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    sql: "str"
    pass_value: "Any"
    tolerance: "Any"
    encryption_configuration: "dict | None"
    gcp_conn_id: "str"
    use_legacy_sql: "bool"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    labels: "dict | None"
    deferrable: "bool"
    poll_interval: "float"


class BigQueryIntervalCheckOperator(
    _BigQueryDbHookMixin,
    SQLIntervalCheckOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    table: "str"
    metrics_thresholds: "dict"
    date_filter_column: "str"
    days_back: "SupportsAbs[int]"
    gcp_conn_id: "str"
    use_legacy_sql: "bool"
    location: "str | None"
    encryption_configuration: "dict | None"
    impersonation_chain: "str | Sequence[str] | None"
    labels: "dict | None"
    deferrable: "bool"
    poll_interval: "float"
    project_id: "str"


class BigQueryColumnCheckOperator(
    _BigQueryDbHookMixin,
    SQLColumnCheckOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    table: "str"
    column_mapping: "dict"
    partition_clause: "str | None"
    database: "str | None"
    accept_none: "bool"
    encryption_configuration: "dict | None"
    gcp_conn_id: "str"
    use_legacy_sql: "bool"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    labels: "dict | None"


class BigQueryTableCheckOperator(
    _BigQueryDbHookMixin,
    SQLTableCheckOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    table: "str"
    checks: "dict"
    partition_clause: "str | None"
    gcp_conn_id: "str"
    use_legacy_sql: "bool"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
    labels: "dict | None"
    encryption_configuration: "dict | None"


class BigQueryGetDataOperator(
    GoogleCloudBaseOperator,
    _BigQueryOperatorsEncryptionConfigurationMixin,
):
    dataset_id: "str | None"
    table_id: "str | None"
    table_project_id: "str | None"
    job_id: "str | None"
    job_project_id: "str | None"
    project_id: "str"
    max_results: "int"
    selected_fields: "str | None"
    gcp_conn_id: "str"
    location: "str | None"
    encryption_configuration: "dict | None"
    impersonation_chain: "str | Sequence[str] | None"
    deferrable: "bool"
    poll_interval: "float"
    as_dict: "bool"
    use_legacy_sql: "bool"


class BigQueryExecuteQueryOperator(GoogleCloudBaseOperator):
    pass


class BigQueryGetDatasetOperator(GoogleCloudBaseOperator):
    dataset_id: "str"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryGetDatasetTablesOperator(GoogleCloudBaseOperator):
    dataset_id: "str"
    project_id: "str"
    max_results: "int | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryPatchDatasetOperator(GoogleCloudBaseOperator):
    pass


class BigQueryUpdateTableOperator(GoogleCloudBaseOperator):
    table_resource: "dict[str, Any]"
    fields: "list[str] | None"
    dataset_id: "str | None"
    table_id: "str | None"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryUpdateDatasetOperator(GoogleCloudBaseOperator):
    dataset_resource: "dict[str, Any]"
    fields: "list[str] | None"
    dataset_id: "str | None"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryDeleteTableOperator(GoogleCloudBaseOperator):
    deletion_dataset_table: "str"
    gcp_conn_id: "str"
    ignore_if_missing: "bool"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryUpsertTableOperator(GoogleCloudBaseOperator):
    dataset_id: "str"
    table_resource: "dict"
    project_id: "str"
    gcp_conn_id: "str"
    location: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class BigQueryUpdateTableSchemaOperator(GoogleCloudBaseOperator):
    schema_fields_updates: "list[dict[str, Any]]"
    dataset_id: "str"
    table_id: "str"
    include_policy_tags: "bool"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    location: "str | None"
