# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class PubSubPullSensor(BaseSensorOperator):
    project_id: "str"
    subscription: "str"
    max_messages: "int"
    ack_messages: "bool"
    gcp_conn_id: "str"
    messages_callback: "Callable[[list[ReceivedMessage], Context], Any] | None"
    impersonation_chain: "str | Sequence[str] | None"
    poke_interval: "float"
    deferrable: "bool"
