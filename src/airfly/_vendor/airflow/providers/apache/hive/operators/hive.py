# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class HiveOperator(BaseOperator):
    hql: "str"
    hive_cli_conn_id: "str"
    schema: "str"
    hiveconfs: "typing.Union[typing.Dict[typing.Any, typing.Any], NoneType]"
    hiveconf_jinja_translate: "bool"
    script_begin_tag: "typing.Union[str, NoneType]"
    run_as_owner: "bool"
    mapred_queue: "typing.Union[str, NoneType]"
    mapred_queue_priority: "typing.Union[str, NoneType]"
    mapred_job_name: "typing.Union[str, NoneType]"
