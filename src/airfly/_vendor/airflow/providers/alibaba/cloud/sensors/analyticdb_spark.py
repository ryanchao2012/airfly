# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class AnalyticDBSparkSensor(BaseSensorOperator):
    app_id: "str"
    adb_spark_conn_id: "str"
    region: "str | None"
