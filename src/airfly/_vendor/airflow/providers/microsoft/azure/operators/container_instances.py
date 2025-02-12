# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class AzureContainerInstancesOperator(BaseOperator):
    ci_conn_id: "str"
    resource_group: "str"
    name: "str"
    image: "str"
    region: "str"
    registry_conn_id: "str | None"
    environment_variables: "dict | None"
    secured_variables: "str | None"
    volumes: "list | None"
    memory_in_gb: "Any | None"
    cpu: "Any | None"
    gpu: "Any | None"
    command: "list[str] | None"
    remove_on_error: "bool"
    fail_if_exists: "bool"
    tags: "dict[str, str] | None"
    os_type: "str"
    restart_policy: "str"
    ip_address: "IpAddress | None"
    ports: "list[ContainerPort] | None"
    subnet_ids: "list[ContainerGroupSubnetId] | None"
    dns_config: "DnsConfiguration | None"
    diagnostics: "ContainerGroupDiagnostics | None"
    priority: "str | None"
