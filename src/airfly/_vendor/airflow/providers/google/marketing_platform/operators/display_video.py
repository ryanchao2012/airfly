# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GoogleDisplayVideo360CreateQueryOperator(BaseOperator):
    body: "dict[str, Any]"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360DeleteReportOperator(BaseOperator):
    report_id: "str | None"
    report_name: "str | None"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360DownloadReportV2Operator(BaseOperator):
    query_id: "str"
    report_id: "str"
    bucket_name: "str"
    report_name: "str | None"
    gzip: "bool"
    chunk_size: "int"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360RunQueryOperator(BaseOperator):
    query_id: "str"
    parameters: "dict[str, Any] | None"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360DownloadLineItemsOperator(BaseOperator):
    request_body: "dict[str, Any]"
    bucket_name: "str"
    object_name: "str"
    gzip: "bool"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360UploadLineItemsOperator(BaseOperator):
    bucket_name: "str"
    object_name: "str"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360CreateSDFDownloadTaskOperator(BaseOperator):
    body_request: "dict[str, Any]"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"


class GoogleDisplayVideo360SDFtoGCSOperator(BaseOperator):
    operation_name: "str"
    bucket_name: "str"
    object_name: "str"
    gzip: "bool"
    api_version: "str"
    gcp_conn_id: "str"
    delegate_to: "str | None"
    impersonation_chain: "str | Sequence[str] | None"
