# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.sagemaker_base import (
    SageMakerBaseOperator,
)


class SageMakerEndpointOperator(SageMakerBaseOperator):
    config: "dict"
    wait_for_completion: "bool"
    check_interval: "int"
    max_ingestion_time: "typing.Union[int, NoneType]"
    operation: "str"
