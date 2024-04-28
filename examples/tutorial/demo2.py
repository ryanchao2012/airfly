from textwrap import dedent

from my_task_model import MyTask


class print_date(MyTask):
    op_params = dict(bash_command="date")


templated_command = dedent(
    """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""
)


class templated(MyTask):
    op_params = dict(
        depends_on_past=False,
        bash_command=templated_command,
        params={"my_param": "Parameter I passed in"},
    )


class sleep(MyTask):
    op_params = dict(depends_on_past=False, bash_command="sleep 5", retries=3)

    upstream = print_date
    downstream = (templated,)
