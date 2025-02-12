# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class AirbyteJobSensor(BaseSensorOperator):
    airbyte_job_id: "int"
    deferrable: "bool"
    airbyte_conn_id: "str"
    api_version: "str"
    api_type: "Literal['config', 'cloud']"
