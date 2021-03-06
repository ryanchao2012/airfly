# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class S3ListOperator(BaseOperator):
    bucket: "str"
    prefix: "str"
    delimiter: "str"
    aws_conn_id: "str"
    verify: "typing.Union[str, bool, NoneType]"
