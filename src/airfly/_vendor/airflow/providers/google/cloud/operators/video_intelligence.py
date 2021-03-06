# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudVideoIntelligenceDetectVideoExplicitContentOperator(BaseOperator):
    input_uri: "str"
    output_uri: "typing.Union[str, NoneType]"
    input_content: "typing.Union[bytes, NoneType]"
    video_context: "typing.Union[typing.Dict, google.cloud.videointelligence_v1.types.VideoContext]"
    location: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudVideoIntelligenceDetectVideoLabelsOperator(BaseOperator):
    input_uri: "str"
    input_content: "typing.Union[bytes, NoneType]"
    output_uri: "typing.Union[str, NoneType]"
    video_context: "typing.Union[typing.Dict, google.cloud.videointelligence_v1.types.VideoContext]"
    location: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudVideoIntelligenceDetectVideoShotsOperator(BaseOperator):
    input_uri: "str"
    output_uri: "typing.Union[str, NoneType]"
    input_content: "typing.Union[bytes, NoneType]"
    video_context: "typing.Union[typing.Dict, google.cloud.videointelligence_v1.types.VideoContext]"
    location: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
