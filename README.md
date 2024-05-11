![](https://github.com/ryanchao2012/airfly/actions/workflows/airfly-run-unittests.yml/badge.svg)
![](https://img.shields.io/pypi/v/airfly.svg)
![](https://img.shields.io/pypi/pyversions/airfly)
![](https://img.shields.io/github/license/ryanchao2012/airfly)


# AirFly: Auto Generate Airflow's `dag.py` On The Fly

Pipeline management is crucial for efficient data operations within a company. Many engineering teams rely on tools like Airflow to help them organize workflows, including ETL processes, reporting pipelines, or machine learning projects.

Airflow offers rich extensibility, allowing developers to arrange workloads into a sequence of tasks. These tasks are then declared within a `DAG` context in a `dag.py` file, specifying task dependencies.

As a workflow grows in complexity, the increasing intricacy of task relations can lead to confusion and disrupt the DAG structure. This complexity often results in decreased code maintainability, particularly in collaborative scenarios.

`airfly` tries to alleviate such pain points and streamline the development life cycle. It operates under the assumption that all tasks are managed within a certain Python module. Developers define task dependencies while creating task objects. During deployment, `airfly` can resolve the dependency tree and automatically generate the `dag.py` for you.

<img src="https://github.com/ryanchao2012/airfly/blob/main/assets/graph-view.png?raw=true" width="800"></img>
***airfly** helps you build complex dags*




## Key Features

* `dag.py` automation: focus on your task, let airfly handle the rest.
* No need to install Airflow: keep your environment lean.
* support task group: a nice feature from Airflow 2.0+
* support duck typing: flexible class inheritance.

## Install

Download `airfly` from PyPI

```
$ pip install airfly

$ airfly --help
Usage: airfly [OPTIONS]

Options:
  --version                   Show version and exit.
  -n, --name TEXT             Assign to DAG id.
  -m, --modname TEXT          Name of the module to search tasks for building
                              the task dependency tree and using it to
                              generate the airflow DAG file.
  -p, --path TEXT             Insert into "sys.path" to include certain
                              modules, multi-value is allowed.
  -e, --exclude-pattern TEXT  Exclude the tasks from the dependency tree if
                              their __qualname__ get matched with this regex
                              pattern.
  -i, --includes TEXT         Paths of python files, the code within will be
                              included in the output DAG file, multi-value is
                              allowed.
  -d, --dag-params TEXT       Parameters to construct DAG object, defined by a
                              dictionary in a python file. Pass this option
                              with <python-file>:<variable> form, the
                              <variable> should be the dictionary which will
                              be passed to DAG as keyword arguments.
  -t, --task-class TEXT       Target task class to search, default:
                              'airfly.model.v1.AirFly'
  -g, --task-group BOOLEAN    Whether to enable TaskGroup, default: True
  --help                      Show this message and exit.
```

## How It Works

`airfly` assumes the tasks are populated in a Python module(or a package, e.g., `man_dag` in the below example), the dependencies are declared by assigning `upstream` or `downstream` attributes to each task. A task holds some attributes corresponding to an airflow operator, when `airfly` walks through the entire module, all tasks are discovered and collected, the dependency tree and the `DAG` context are auto-built, with some `ast` helpers, `airfly` can wrap the information, convert it into python code, and finally save them to `dag.py`.

```sh
main_dag
├── __init__.py
├── mod_a.py
│   ├── task_a1
│   └── task_a2
│       └── upstream: task_a1
├── mod_b.py
│   └── task_b1
│       └── downstream: task_a1, task_a2
├── sub_dag
│   ├── __init__.py
│   ├── mod_c.py
:   :
```


### Define your task with `AirFly`

Declare a task as following(see [demo](https://github.com/ryanchao2012/airfly/blob/main/examples/tutorial/demo.py)):

```python
# in demo.py
from airfly.model import AirFly


class print_date(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="date")


# during dag generation,
# this class will be converted to airflow operator
print_date._to_ast(print_date).show()
# examples_tutorial_demo_print_date = BashOperator(
#     task_id='examples.tutorial.demo.print_date',
#     bash_command='date',
#     task_group=group_examples_tutorial_demo
# )

```

* `op_class (str)`: specifies the airflow operator to this task.
* `op_params`: keyword arguments which will be passed to the airflow operator(`op_class`), a parameter (i.e., value in the dictionary) could be one of the [primitive types](https://docs.python.org/3/library/stdtypes.html), a function or a class.

You can also define the attributes by `property`:
```python
from airfly.model import AirFly


class print_date(AirFly):

    @property
    def op_class(self):
        return "BashOperator"

    @property
    def op_params(self):
        return dict(bash_command="date")

print_date._to_ast(print_date).show()
# examples_tutorial_demo_print_date = BashOperator(
#     task_id='examples.tutorial.demo.print_date',
#     bash_command='date',
#     task_group=group_examples_tutorial_demo
# )

```

By default, the class name(`print_date`) maps to `task_id` to the applied operator after dag generation. You can change this behavior by overriding `_get_taskid` as a classmethod, you have to make sure the task id is globally unique:

```python

from airfly.model import AirFly


class print_date(AirFly):
    @classmethod
    def _get_taskid(cls):
        # customize the task id
        return f"my_task_{cls.__qualname__}"
    op_class = "BashOperator" 
    op_params = dict(bash_command="date")


print_date._to_ast(print_date).show()
# my_task_print_date = BashOperator(
#     task_id='my_task_print_date',
#     bash_command='date',
#     task_group=group_my_task_print_date
# )

```


### Define task dependency

Specifying task dependency with `upstream` or `downstream`.

```python
# in demo.py

from textwrap import dedent


templated_command = dedent(
    """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""
)

class templated(AirFly):
    op_class = "BashOperator"
    op_params = dict(depends_on_past=False,
                  bash_command=templated_command,
                  params={"my_param": "Parameter I passed in"})


class sleep(AirFly):
    op_class = "BashOperator"
    op_params = dict(depends_on_past=False, 
                  bash_command="sleep 5",
                  retries=3)

    upstream = print_date

    @property   # property also works
    def downstream(self):
        return (templated,)
```

`upstream`/`downstream`: return a task class or a iterable such as list or tuple.


### Generate `dag.py`
Generate the dag by the command:
```sh
$ airfly --name demo_dag --modname demo > dag.py
```

Output in `dag.py`:

```python
# This file is auto-generated by airfly 1.0.0
from airflow.models import DAG
from airflow.utils.task_group import TaskGroup

with DAG("demo_dag") as dag:
    from airflow.operators.bash import BashOperator

    group_demo = TaskGroup(group_id="demo", prefix_group_id=False)
    demo_print_date = BashOperator(
        task_id="demo.print_date", bash_command="date", task_group=group_demo
    )
    demo_sleep = BashOperator(
        task_id="demo.sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
        task_group=group_demo,
    )
    demo_templated = BashOperator(
        task_id="demo.templated",
        depends_on_past=False,
        bash_command='\n{% for i in range(5) %}\n    echo "{{ ds }}"\n    echo "{{ macros.ds_add(ds, 7)}}"\n    echo "{{ params.my_param }}"\n{% endfor %}\n',
        params={"my_param": "Parameter I passed in"},
        task_group=group_demo,
    )
    demo_print_date >> demo_sleep
    demo_sleep >> demo_templated
```

Make sure the `demo` module is in the current environment so that `airfly` can find it.
If it's not the case, you can use `--path/-p` to add the location of the module into `sys.path`, e.g.,

```sh
.
├── folder
│   └── subfolder
│       └── demo.py   # Assume this is the target module
:

$ airfly --name demo_dag --path folder/subfolder --modname demo > dag.py
```

The target module can be a package as well, e.g.,

```sh
.
├── folder
│   └── subfolder
│       └── demo   # Assume this is the target package
│           ├── __init__.py
│           ├── module_a.py
:           :

$ airfly --name demo_dag --path folder/subfolder --modname demo > dag.py
```


## Inject parameters to `DAG`

Manage the DAG arguments in a python file(see [demo](https://github.com/ryanchao2012/airfly/blob/main/examples/tutorial/params.py)), then pass them to `airfly`.

```python
# in params.py

from datetime import timedelta

from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag_kwargs = dict(
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)
```

Inject the arguments by passing `--dag-params` option, with the format of `<python-file>:<variable>`:
```
$ airfly --name demo_dag --modname demo --dag-params params.py:dag_kwargs > dag.py
```

Output in `dag.py`:

```python
# This file is auto-generated by airfly 1.0.0
from datetime import timedelta

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

# >>>>>>>>>> Include from 'params.py'
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
dag_kwargs = dict(
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)
# <<<<<<<<<< End of code insertion
with DAG("demo_dag", **dag_kwargs) as dag:
    from airflow.operators.bash import BashOperator

    group_demo = TaskGroup(group_id="demo", prefix_group_id=False)
    demo_print_date = BashOperator(
        task_id="demo.print_date", bash_command="date", task_group=group_demo
    )
    demo_sleep = BashOperator(
        task_id="demo.sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
        task_group=group_demo,
    )
    demo_templated = BashOperator(
        task_id="demo.templated",
        depends_on_past=False,
        bash_command='\n{% for i in range(5) %}\n    echo "{{ ds }}"\n    echo "{{ macros.ds_add(ds, 7)}}"\n    echo "{{ params.my_param }}"\n{% endfor %}\n',
        params={"my_param": "Parameter I passed in"},
        task_group=group_demo,
    )
    demo_print_date >> demo_sleep
    demo_sleep >> demo_templated

```

`airfly` wraps required information including variables and imports into output python script, and pass the specified value to `DAG` object.


## Exclude tasks from codegen
By passing `--exclude-pattern` to match any unwanted objects with their `__qualname__`. then filter them out.

```
$ airfly --name demo_dag --modname demo --exclude-pattern templated > dag.py
```

Output in `dag.py`:

```python
# This file is auto-generated by airfly 1.0.0
from airflow.models import DAG
from airflow.utils.task_group import TaskGroup

with DAG("demo_dag") as dag:
    from airflow.operators.bash import BashOperator

    group_demo = TaskGroup(group_id="demo", prefix_group_id=False)
    demo_print_date = BashOperator(
        task_id="demo.print_date", bash_command="date", task_group=group_demo
    )
    demo_sleep = BashOperator(
        task_id="demo.sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
        task_group=group_demo,
    )
    demo_print_date >> demo_sleep

```

The `templated` task is gone.


### Task Group

`airfly`  defines `TaskGroup` in the DAG context and assigns `task_group` to each operator for you.
It maps the module hierarchy to the nested group structure,
so the tasks in the same python module will be grouped closer.
If you don't like this feature, pass `--task-group`/`-g` with `False` to disable it. 


## Duck Typing

In fact, there's no need to inherite from `AirFly`, you can have your own task class definition, as long as it provides certain attributes, `airfly` can still work for you.


```python
# my_task_model.py
from typing import Any, Dict, Iterable, Type, Union

TaskClass = Type["MyTask"]


class MyTask:
    # airfly assumes these attributes exist
    op_class: str = "BashOperator"
    op_params: Dict[str, Any] = None
    op_module: str = None
    upstream: Union[TaskClass, Iterable[TaskClass]] = None
    downstream: Union[TaskClass, Iterable[TaskClass]] = None

    # other stuffs


# in demo2.py
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
```

Pass the task definition with `--task-class`

```
$ airfly --name demo_dag --modname demo2 --task-class my_task_model.MyTask > dag.py
```

Output in `dag.py`:

```python
# This file is auto-generated by airfly 1.0.0
from airflow.models import DAG
from airflow.utils.task_group import TaskGroup

with DAG("demo_dag") as dag:
    from airflow.operators.bash import BashOperator

    group_demo2 = TaskGroup(group_id="demo2", prefix_group_id=False)
    demo2_print_date = BashOperator(
        task_id="demo2.print_date", bash_command="date", task_group=group_demo2
    )
    demo2_sleep = BashOperator(
        task_id="demo2.sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
        task_group=group_demo2,
    )
    demo2_templated = BashOperator(
        task_id="demo2.templated",
        depends_on_past=False,
        bash_command='\n{% for i in range(5) %}\n    echo "{{ ds }}"\n    echo "{{ macros.ds_add(ds, 7)}}"\n    echo "{{ params.my_param }}"\n{% endfor %}\n',
        params={"my_param": "Parameter I passed in"},
        task_group=group_demo2,
    )
    demo2_print_date >> demo2_sleep
    demo2_sleep >> demo2_templated
```


## Examples

Please explore more examples [here](https://github.com/ryanchao2012/airfly/blob/main/examples).

