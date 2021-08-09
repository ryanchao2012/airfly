# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class JenkinsJobTriggerOperator(BaseOperator):
    jenkins_connection_id: "str"
    job_name: "str"
    parameters: "typing.Union[str, typing.Dict, typing.List, NoneType]"
    sleep_time: "int"
    max_try_before_job_appears: "int"
    allowed_jenkins_states: "typing.Union[typing.Iterable[str], NoneType]"