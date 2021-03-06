# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GCSToS3Operator(BaseOperator):
    bucket: "str"
    prefix: "typing.Union[str, NoneType]"
    delimiter: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    google_cloud_storage_conn_id: "typing.Union[str, NoneType]"
    delegate_to: "typing.Union[str, NoneType]"
    dest_aws_conn_id: "str"
    dest_s3_key: "str"
    dest_verify: "typing.Union[str, bool, NoneType]"
    replace: "bool"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
    dest_s3_extra_args: "typing.Union[typing.Dict, NoneType]"
    s3_acl_policy: "typing.Union[str, NoneType]"
