# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DockerOperator(BaseOperator):
    image: "str"
    api_version: "str | None"
    command: "str | list[str] | None"
    container_name: "str | None"
    cpus: "float"
    docker_url: "str | list[str] | None"
    environment: "dict | None"
    private_environment: "dict | None"
    env_file: "str | None"
    force_pull: "bool"
    mem_limit: "float | str | None"
    host_tmp_dir: "str | None"
    network_mode: "str | None"
    tls_ca_cert: "str | None"
    tls_client_cert: "str | None"
    tls_client_key: "str | None"
    tls_verify: "bool"
    tls_hostname: "str | bool | None"
    tls_ssl_version: "str | None"
    mount_tmp_dir: "bool"
    tmp_dir: "str"
    user: "str | int | None"
    mounts: "list[Mount] | None"
    entrypoint: "str | list[str] | None"
    working_dir: "str | None"
    xcom_all: "bool"
    docker_conn_id: "str | None"
    dns: "list[str] | None"
    dns_search: "list[str] | None"
    auto_remove: "Literal['never', 'success', 'force']"
    shm_size: "int | None"
    tty: "bool"
    hostname: "str | None"
    privileged: "bool"
    cap_add: "Iterable[str] | None"
    extra_hosts: "dict[str, str] | None"
    retrieve_output: "bool"
    retrieve_output_path: "str | None"
    timeout: "int"
    device_requests: "list[DeviceRequest] | None"
    log_opts_max_size: "str | None"
    log_opts_max_file: "str | None"
    ipc_mode: "str | None"
    skip_on_exit_code: "int | Container[int] | None"
    port_bindings: "dict | None"
    ulimits: "list[Ulimit] | None"
    skip_exit_code: "int | Container[int] | ArgNotSet"
