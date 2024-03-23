# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class CloudNaturalLanguageAnalyzeEntitiesOperator(GoogleCloudBaseOperator):
    document: "dict | Document"
    encoding_type: "EncodingType | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "MetaData"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudNaturalLanguageAnalyzeEntitySentimentOperator(GoogleCloudBaseOperator):
    document: "dict | Document"
    encoding_type: "EncodingType | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "MetaData"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudNaturalLanguageAnalyzeSentimentOperator(GoogleCloudBaseOperator):
    document: "dict | Document"
    encoding_type: "EncodingType | None"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "MetaData"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class CloudNaturalLanguageClassifyTextOperator(GoogleCloudBaseOperator):
    document: "dict | Document"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "MetaData"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
