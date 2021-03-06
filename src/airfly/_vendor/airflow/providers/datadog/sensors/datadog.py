# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class DatadogSensor(BaseSensorOperator):
    datadog_conn_id: "str"
    from_seconds_ago: "int"
    up_to_seconds_from_now: "int"
    priority: "typing.Union[str, NoneType]"
    sources: "typing.Union[str, NoneType]"
    tags: "typing.Union[typing.List[str], NoneType]"
    response_check: "typing.Union[typing.Callable[[typing.Dict[str, typing.Any]], bool], NoneType]"
