# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DataprocCreateClusterOperator(BaseOperator):
    folder_id: "str | None"
    cluster_name: "str | None"
    cluster_description: "str | None"
    cluster_image_version: "str | None"
    ssh_public_keys: "str | Iterable[str] | None"
    subnet_id: "str | None"
    services: "Iterable[str]"
    s3_bucket: "str | None"
    zone: "str"
    service_account_id: "str | None"
    masternode_resource_preset: "str | None"
    masternode_disk_size: "int | None"
    masternode_disk_type: "str | None"
    datanode_resource_preset: "str | None"
    datanode_disk_size: "int | None"
    datanode_disk_type: "str | None"
    datanode_count: "int"
    computenode_resource_preset: "str | None"
    computenode_disk_size: "int | None"
    computenode_disk_type: "str | None"
    computenode_count: "int"
    computenode_max_hosts_count: "int | None"
    computenode_measurement_duration: "int | None"
    computenode_warmup_duration: "int | None"
    computenode_stabilization_duration: "int | None"
    computenode_preemptible: "bool"
    computenode_cpu_utilization_target: "int | None"
    computenode_decommission_timeout: "int | None"
    connection_id: "str | None"
    properties: "dict[str, str] | None"
    enable_ui_proxy: "bool"
    host_group_ids: "Iterable[str] | None"
    security_group_ids: "Iterable[str] | None"
    log_group_id: "str | None"
    initialization_actions: "Iterable[InitializationAction] | None"
    labels: "dict[str, str] | None"


class DataprocBaseOperator(BaseOperator):
    yandex_conn_id: "str | None"
    cluster_id: "str | None"


class DataprocDeleteClusterOperator(DataprocBaseOperator):
    connection_id: "str | None"
    cluster_id: "str | None"


class DataprocCreateHiveJobOperator(DataprocBaseOperator):
    query: "str | None"
    query_file_uri: "str | None"
    script_variables: "dict[str, str] | None"
    continue_on_failure: "bool"
    properties: "dict[str, str] | None"
    name: "str"
    cluster_id: "str | None"
    connection_id: "str | None"


class DataprocCreateMapReduceJobOperator(DataprocBaseOperator):
    main_class: "str | None"
    main_jar_file_uri: "str | None"
    jar_file_uris: "Iterable[str] | None"
    archive_uris: "Iterable[str] | None"
    file_uris: "Iterable[str] | None"
    args: "Iterable[str] | None"
    properties: "dict[str, str] | None"
    name: "str"
    cluster_id: "str | None"
    connection_id: "str | None"


class DataprocCreateSparkJobOperator(DataprocBaseOperator):
    main_class: "str | None"
    main_jar_file_uri: "str | None"
    jar_file_uris: "Iterable[str] | None"
    archive_uris: "Iterable[str] | None"
    file_uris: "Iterable[str] | None"
    args: "Iterable[str] | None"
    properties: "dict[str, str] | None"
    name: "str"
    cluster_id: "str | None"
    connection_id: "str | None"
    packages: "Iterable[str] | None"
    repositories: "Iterable[str] | None"
    exclude_packages: "Iterable[str] | None"


class DataprocCreatePysparkJobOperator(DataprocBaseOperator):
    main_python_file_uri: "str | None"
    python_file_uris: "Iterable[str] | None"
    jar_file_uris: "Iterable[str] | None"
    archive_uris: "Iterable[str] | None"
    file_uris: "Iterable[str] | None"
    args: "Iterable[str] | None"
    properties: "dict[str, str] | None"
    name: "str"
    cluster_id: "str | None"
    connection_id: "str | None"
    packages: "Iterable[str] | None"
    repositories: "Iterable[str] | None"
    exclude_packages: "Iterable[str] | None"
