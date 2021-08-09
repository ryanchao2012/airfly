# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.pubsub import (
    PubSubCreateSubscriptionOperator,
    PubSubCreateTopicOperator,
    PubSubDeleteSubscriptionOperator,
    PubSubDeleteTopicOperator,
    PubSubPublishMessageOperator,
)


class PubSubPublishOperator(PubSubPublishMessageOperator):
    pass


class PubSubSubscriptionCreateOperator(PubSubCreateSubscriptionOperator):
    pass


class PubSubSubscriptionDeleteOperator(PubSubDeleteSubscriptionOperator):
    pass


class PubSubTopicCreateOperator(PubSubCreateTopicOperator):
    pass


class PubSubTopicDeleteOperator(PubSubDeleteTopicOperator):
    pass
