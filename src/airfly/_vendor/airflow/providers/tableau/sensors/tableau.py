# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class TableauJobStatusSensor(BaseSensorOperator):
    job_id: "str"
    site_id: "str | None"
    tableau_conn_id: "str"
