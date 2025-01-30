# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class KubernetesResourceBaseOperator(BaseOperator):
    yaml_conf: "str | None"
    yaml_conf_file: "str | None"
    namespace: "str | None"
    kubernetes_conn_id: "str | None"
    custom_resource_definition: "bool"
    namespaced: "bool"
    config_file: "str | None"


class KubernetesCreateResourceOperator(KubernetesResourceBaseOperator):
    yaml_conf: "str | None"
    yaml_conf_file: "str | None"
    namespace: "str | None"
    kubernetes_conn_id: "str | None"
    custom_resource_definition: "bool"
    namespaced: "bool"
    config_file: "str | None"


class KubernetesDeleteResourceOperator(KubernetesResourceBaseOperator):
    yaml_conf: "str | None"
    yaml_conf_file: "str | None"
    namespace: "str | None"
    kubernetes_conn_id: "str | None"
    custom_resource_definition: "bool"
    namespaced: "bool"
    config_file: "str | None"
