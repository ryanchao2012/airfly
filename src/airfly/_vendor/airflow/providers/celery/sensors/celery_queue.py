# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class CeleryQueueSensor(BaseSensorOperator):
    celery_queue: "str"
    target_task_id: "str | None"
