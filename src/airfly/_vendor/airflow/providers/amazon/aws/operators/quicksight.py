# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.base_aws import (
    AwsBaseOperator,
)


class QuickSightCreateIngestionOperator(AwsBaseOperator):
    data_set_id: "str"
    ingestion_id: "str"
    ingestion_type: "str"
    wait_for_completion: "bool"
    check_interval: "int"
