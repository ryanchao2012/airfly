# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SQSPublishOperator(BaseOperator):
    sqs_queue: "str"
    message_content: "str"
    message_attributes: "typing.Union[dict, NoneType]"
    delay_seconds: "int"
    aws_conn_id: "str"
