# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class EmailOperator(BaseOperator):
    to: "typing.Union[typing.List[str], str]"
    subject: "str"
    html_content: "str"
    files: "typing.Union[typing.List, NoneType]"
    cc: "typing.Union[str, typing.List[str], NoneType]"
    bcc: "typing.Union[str, typing.List[str], NoneType]"
    mime_subtype: "str"
    mime_charset: "str"
    conn_id: "typing.Union[str, NoneType]"
