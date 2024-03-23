# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class BashOperator(BaseOperator):
    bash_command: "str"
    env: "dict[str, str] | None"
    append_env: "bool"
    output_encoding: "str"
    skip_exit_code: "int | None"
    skip_on_exit_code: "int | Container[int] | None"
    cwd: "str | None"
