# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class BigtableValidationMixin:
    pass


class BigtableCreateInstanceOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    main_cluster_id: "str"
    main_cluster_zone: "str"
    project_id: "str"
    replica_clusters: "list[dict[str, str]] | None"
    instance_display_name: "str | None"
    instance_type: "enums.Instance.Type | None"
    instance_labels: "dict | None"
    cluster_nodes: "int | None"
    cluster_storage_type: "enums.StorageType | None"
    timeout: "float | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigtableUpdateInstanceOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    project_id: "str"
    instance_display_name: "str | None"
    instance_type: "enums.Instance.Type | enum.IntEnum | None"
    instance_labels: "dict | None"
    timeout: "float | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigtableDeleteInstanceOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigtableCreateTableOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    table_id: "str"
    project_id: "str"
    initial_split_keys: "list | None"
    column_families: "dict[str, GarbageCollectionRule] | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigtableDeleteTableOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    table_id: "str"
    project_id: "str"
    app_profile_id: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class BigtableUpdateClusterOperator(GoogleCloudBaseOperator, BigtableValidationMixin):
    instance_id: "str"
    cluster_id: "str"
    nodes: "int"
    project_id: "str"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
