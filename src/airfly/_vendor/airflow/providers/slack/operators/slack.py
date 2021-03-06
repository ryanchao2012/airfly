# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SlackAPIOperator(BaseOperator):
    slack_conn_id: "typing.Union[str, NoneType]"
    token: "typing.Union[str, NoneType]"
    method: "typing.Union[str, NoneType]"
    api_params: "typing.Union[typing.Dict, NoneType]"


class SlackAPIPostOperator(SlackAPIOperator):
    channel: "str"
    username: "str"
    text: "str"
    icon_url: "str"
    attachments: "typing.Union[typing.List, NoneType]"
    blocks: "typing.Union[typing.List, NoneType]"
