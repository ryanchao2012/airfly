from airfly.model import AirFly


class run_this_last(AirFly):
    op_class = "EmptyOperator"


class run_this(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo 1")
    downstream = run_this_last


class runme_0(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command='echo "{{ task_instance_key_str }}" && sleep 1')
    downstream = run_this


class runme_1(runme_0):
    pass


class runme_2(runme_0):
    pass


class also_run_this(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"')
    downstream = run_this_last


class this_will_skip(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command='echo "hello world"; exit 99;')
    downstream = run_this_last
