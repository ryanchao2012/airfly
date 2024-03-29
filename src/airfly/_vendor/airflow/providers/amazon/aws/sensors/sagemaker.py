# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class SageMakerBaseSensor(BaseSensorOperator):
    aws_conn_id: "str | None"
    resource_type: "str"


class SageMakerEndpointSensor(SageMakerBaseSensor):
    endpoint_name: "_empty"


class SageMakerTransformSensor(SageMakerBaseSensor):
    job_name: "str"


class SageMakerTuningSensor(SageMakerBaseSensor):
    job_name: "str"


class SageMakerTrainingSensor(SageMakerBaseSensor):
    job_name: "_empty"
    print_log: "_empty"


class SageMakerPipelineSensor(SageMakerBaseSensor):
    pipeline_exec_arn: "str"
    verbose: "bool"


class SageMakerAutoMLSensor(SageMakerBaseSensor):
    job_name: "str"
