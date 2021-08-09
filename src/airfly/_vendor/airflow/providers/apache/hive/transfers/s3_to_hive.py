# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class S3ToHiveOperator(BaseOperator):
    s3_key: "str"
    field_dict: "typing.Dict"
    hive_table: "str"
    delimiter: "str"
    create: "bool"
    recreate: "bool"
    partition: "typing.Union[typing.Dict, NoneType]"
    headers: "bool"
    check_headers: "bool"
    wildcard_match: "bool"
    aws_conn_id: "str"
    verify: "typing.Union[bool, str, NoneType]"
    hive_cli_conn_id: "str"
    input_compressed: "bool"
    tblproperties: "typing.Union[typing.Dict, NoneType]"
    select_expression: "typing.Union[str, NoneType]"
