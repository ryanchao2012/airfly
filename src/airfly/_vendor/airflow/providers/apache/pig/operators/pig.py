# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class PigOperator(BaseOperator):
    pig: "str"
    pig_cli_conn_id: "str"
    pigparams_jinja_translate: "bool"
    pig_opts: "typing.Union[str, NoneType]"
