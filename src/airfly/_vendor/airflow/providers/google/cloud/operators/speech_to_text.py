# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudSpeechToTextRecognizeSpeechOperator(BaseOperator):
    audio: "RecognitionAudio"
    config: "RecognitionConfig"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
