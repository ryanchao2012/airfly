"""
A simple workflow for demo, fork from https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
"""

from textwrap import dedent

from airfly.model.airflow import AirflowTask


class print_date(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="date")


templated_command = dedent(
    """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""
)


class templated(AirflowTask):
    operator_class = "BashOperator"
    params = dict(
        depends_on_past=False,
        bash_command=templated_command,
        params={"my_param": "Parameter I passed in"},
    )


class sleep(AirflowTask):
    operator_class = "BashOperator"
    params = dict(depends_on_past=False, bash_command="sleep 5", retries=3)

    upstream = print_date
    downstream = (templated,)
