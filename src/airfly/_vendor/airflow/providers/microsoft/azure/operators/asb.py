# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class AzureServiceBusCreateQueueOperator(BaseOperator):
    queue_name: "str"
    max_delivery_count: "int"
    dead_lettering_on_message_expiration: "bool"
    enable_batched_operations: "bool"
    azure_service_bus_conn_id: "str"


class AzureServiceBusSendMessageOperator(BaseOperator):
    queue_name: "str"
    message: "str | list[str]"
    batch: "bool"
    azure_service_bus_conn_id: "str"


class AzureServiceBusReceiveMessageOperator(BaseOperator):
    queue_name: "str"
    azure_service_bus_conn_id: "str"
    max_message_count: "int"
    max_wait_time: "float"


class AzureServiceBusDeleteQueueOperator(BaseOperator):
    queue_name: "str"
    azure_service_bus_conn_id: "str"


class AzureServiceBusTopicCreateOperator(BaseOperator):
    topic_name: "str"
    azure_service_bus_conn_id: "str"
    default_message_time_to_live: "datetime.timedelta | str | None"
    max_size_in_megabytes: "int | None"
    requires_duplicate_detection: "bool | None"
    duplicate_detection_history_time_window: "datetime.timedelta | str | None"
    enable_batched_operations: "bool | None"
    size_in_bytes: "int | None"
    filtering_messages_before_publishing: "bool | None"
    authorization_rules: "list[AuthorizationRule] | None"
    support_ordering: "bool | None"
    auto_delete_on_idle: "datetime.timedelta | str | None"
    enable_partitioning: "bool | None"
    enable_express: "bool | None"
    user_metadata: "str | None"
    max_message_size_in_kilobytes: "int | None"


class AzureServiceBusSubscriptionCreateOperator(BaseOperator):
    topic_name: "str"
    subscription_name: "str"
    azure_service_bus_conn_id: "str"
    lock_duration: "datetime.timedelta | str | None"
    requires_session: "bool | None"
    default_message_time_to_live: "datetime.timedelta | str | None"
    dead_lettering_on_message_expiration: "bool | None"
    dead_lettering_on_filter_evaluation_exceptions: "bool | None"
    max_delivery_count: "int | None"
    enable_batched_operations: "bool | None"
    forward_to: "str | None"
    user_metadata: "str | None"
    forward_dead_lettered_messages_to: "str | None"
    auto_delete_on_idle: "datetime.timedelta | str | None"


class AzureServiceBusUpdateSubscriptionOperator(BaseOperator):
    topic_name: "str"
    subscription_name: "str"
    max_delivery_count: "int | None"
    dead_lettering_on_message_expiration: "bool | None"
    enable_batched_operations: "bool | None"
    azure_service_bus_conn_id: "str"


class ASBReceiveSubscriptionMessageOperator(BaseOperator):
    topic_name: "str"
    subscription_name: "str"
    max_message_count: "int | None"
    max_wait_time: "float | None"
    azure_service_bus_conn_id: "str"


class AzureServiceBusSubscriptionDeleteOperator(BaseOperator):
    topic_name: "str"
    subscription_name: "str"
    azure_service_bus_conn_id: "str"


class AzureServiceBusTopicDeleteOperator(BaseOperator):
    topic_name: "str"
    azure_service_bus_conn_id: "str"
