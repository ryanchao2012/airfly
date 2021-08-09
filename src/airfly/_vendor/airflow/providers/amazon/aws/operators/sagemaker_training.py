# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.sagemaker_base import (
    SageMakerBaseOperator,
)


class SageMakerTrainingOperator(SageMakerBaseOperator):
    config: "dict"
    wait_for_completion: "bool"
    print_log: "bool"
    check_interval: "int"
    max_ingestion_time: "typing.Union[int, NoneType]"
    check_if_job_exists: "bool"
    action_if_job_exists: "str"
