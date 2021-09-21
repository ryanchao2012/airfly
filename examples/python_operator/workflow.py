import time
from pprint import pprint

from airfly.model.airflow import AirflowTask


def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    pprint(kwargs)
    print(ds)
    return "Whatever you return gets printed in the logs"


def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    time.sleep(random_base)


def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.
    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    for _ in range(10):
        print(Style.DIM + "Please wait...", flush=True)
        sleep(10)
    print("Finished")


class run_this(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_context)


# TODO: how to dynamically create task class?
class sleep_for_0(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=my_sleeping_function, op_kwargs={"random_base": 0})
    upstreams = run_this


class sleep_for_1(sleep_for_0):
    params = dict(python_callable=my_sleeping_function, op_kwargs={"random_base": 1})


class sleep_for_2(sleep_for_0):
    params = dict(python_callable=my_sleeping_function, op_kwargs={"random_base": 2})


class sleep_for_3(sleep_for_0):
    params = dict(python_callable=my_sleeping_function, op_kwargs={"random_base": 3})


class sleep_for_4(sleep_for_0):
    params = dict(python_callable=my_sleeping_function, op_kwargs={"random_base": 4})


class virtualenv_task(AirflowTask):
    operator_class = "PythonVirtualenvOperator"
    params = dict(
        python_callable=callable_virtualenv,
        requirements=["colorama==0.4.0"],
        system_site_packages=False,
    )
