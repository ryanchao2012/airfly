# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class ECSOperator(BaseOperator):
    task_definition: "str"
    cluster: "str"
    overrides: "dict"
    aws_conn_id: "typing.Union[str, NoneType]"
    region_name: "typing.Union[str, NoneType]"
    launch_type: "str"
    capacity_provider_strategy: "typing.Union[list, NoneType]"
    group: "typing.Union[str, NoneType]"
    placement_constraints: "typing.Union[list, NoneType]"
    placement_strategy: "typing.Union[list, NoneType]"
    platform_version: "str"
    network_configuration: "typing.Union[dict, NoneType]"
    tags: "typing.Union[dict, NoneType]"
    awslogs_group: "typing.Union[str, NoneType]"
    awslogs_region: "typing.Union[str, NoneType]"
    awslogs_stream_prefix: "typing.Union[str, NoneType]"
    propagate_tags: "typing.Union[str, NoneType]"
    quota_retry: "typing.Union[dict, NoneType]"
    reattach: "bool"
