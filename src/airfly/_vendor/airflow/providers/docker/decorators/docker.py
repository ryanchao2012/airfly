# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.decorators.base import DecoratedOperator
from airfly._vendor.airflow.providers.docker.operators.docker import DockerOperator


class _DockerDecoratedOperator(DecoratedOperator, DockerOperator):
    use_dill: "_empty"
    python_command: "_empty"
    expect_airflow: "bool"
