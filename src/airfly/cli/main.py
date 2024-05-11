import importlib
import os

import click

from airfly.model import AirFly, TaskTree
from airfly.utils import qualname

from .utils import (
    convert_dag_params,
    convert_task_group,
    expand_sys_path,
    print_version,
    validate_includes,
)


@click.command()
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show version and exit.",
)
@click.option("--name", "-n", help="Assign to DAG id.")
@click.option(
    "--modname",
    "-m",
    help=(
        "Name of the module to search tasks"
        " for building the task dependency tree"
        " and using it to generate the airflow DAG file."
    ),
)
@click.option(
    "--path",
    "-p",
    multiple=True,
    default=[os.getcwd()],
    help='Insert into "sys.path" to include certain modules, multi-value is allowed.',
)
@click.option(
    "--exclude-pattern",
    "-e",
    help=(
        "Exclude the tasks from the dependency tree"
        " if their __qualname__ get matched with this regex pattern."
    ),
)
@click.option(
    "--includes",
    "-i",
    callback=validate_includes,
    help=(
        "Paths of python files, the code within"
        " will be included in the output DAG file, multi-value is allowed."
    ),
    multiple=True,
)
@click.option(
    "--dag-params",
    "-d",
    callback=convert_dag_params,
    help=(
        "Parameters to construct DAG object,"
        " defined by a dictionary in a python file."
        " Pass this option with <python-file>:<variable> form,"
        " the <variable> should be the dictionary"
        " which will be passed to DAG as keyword arguments."
    ),
)
@click.option(
    "--task-class",
    "-t",
    default="airfly.model.AirFly",
    help=f"Target task class to search, default: '{qualname(AirFly)}'",
)
@click.option(
    "--task-group",
    "-g",
    callback=convert_task_group,
    default=True,
    help="Whether to enable TaskGroup, default: True",
)
def main(
    name, modname, path, exclude_pattern, includes, dag_params, task_class, task_group
):

    with expand_sys_path(*path):
        module = importlib.import_module(modname)

        taskmodule, taskname = task_class.rsplit(".", 1)
        taskmodule = importlib.import_module(taskmodule)
        taskclass = taskmodule.__dict__[taskname]

    name = name or f"{modname}_dag"

    if dag_params and dag_params[0]:
        if includes:
            includes.append(dag_params[0])
        else:
            includes = [dag_params[0]]

    tree = TaskTree.from_module(
        module, taskclass=taskclass, exclude_pattern=exclude_pattern
    )

    print(
        tree.to_dag(
            name, includes=includes, dag_params=dag_params, task_group=task_group
        ),
        end="",
    )
