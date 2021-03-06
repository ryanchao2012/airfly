# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class SubDagOperator(BaseSensorOperator):
    subdag: "DAG"
    session: "typing.Union[sqlalchemy.orm.session.Session, NoneType]"
    conf: "typing.Union[typing.Dict, NoneType]"
    propagate_skipped_state: "typing.Union[airflow.operators.subdag.SkippedStatePropagationOptions, NoneType]"
