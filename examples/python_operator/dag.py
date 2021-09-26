# This file is auto-generated by airfly 0.5.0
from datetime import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

from workflow import callable_virtualenv, my_sleeping_function, print_context

# >>>>>>>>>> Include from 'params.py'
dag_kwargs = dict(
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
)
# <<<<<<<<<< End of code insertion
with DAG("example_python_operator", **dag_kwargs) as dag:
    workflow_run_this = PythonOperator(
        task_id="workflow.run_this", python_callable=print_context
    )
    workflow_sleep_for_0 = PythonOperator(
        task_id="workflow.sleep_for_0",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 0},
    )
    workflow_sleep_for_1 = PythonOperator(
        task_id="workflow.sleep_for_1",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 1},
    )
    workflow_sleep_for_2 = PythonOperator(
        task_id="workflow.sleep_for_2",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 2},
    )
    workflow_sleep_for_3 = PythonOperator(
        task_id="workflow.sleep_for_3",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 3},
    )
    workflow_sleep_for_4 = PythonOperator(
        task_id="workflow.sleep_for_4",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 4},
    )
    workflow_virtualenv_task = PythonVirtualenvOperator(
        task_id="workflow.virtualenv_task",
        python_callable=callable_virtualenv,
        requirements=["colorama==0.4.0"],
        system_site_packages=False,
    )
    workflow_run_this >> workflow_sleep_for_0
    workflow_run_this >> workflow_sleep_for_1
    workflow_run_this >> workflow_sleep_for_2
    workflow_run_this >> workflow_sleep_for_3
    workflow_run_this >> workflow_sleep_for_4