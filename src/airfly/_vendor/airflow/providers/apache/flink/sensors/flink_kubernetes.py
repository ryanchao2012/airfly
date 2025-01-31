# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class FlinkKubernetesSensor(BaseSensorOperator):
    application_name: "str"
    attach_log: "bool"
    namespace: "str | None"
    kubernetes_conn_id: "str"
    api_group: "str"
    api_version: "str"
    plural: "str"
