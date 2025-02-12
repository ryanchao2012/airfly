# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class FlinkKubernetesOperator(BaseOperator):
    application_file: "str"
    namespace: "str | None"
    kubernetes_conn_id: "str"
    api_group: "str"
    api_version: "str"
    in_cluster: "bool | None"
    cluster_context: "str | None"
    config_file: "str | None"
    plural: "str"
