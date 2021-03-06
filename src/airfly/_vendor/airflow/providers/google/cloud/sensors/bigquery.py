# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class BigQueryTableExistenceSensor(BaseSensorOperator):
    project_id: "str"
    dataset_id: "str"
    table_id: "str"
    bigquery_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
