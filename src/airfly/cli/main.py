import os

import click
from airfly.model.airflow import AirflowDAG, AirflowTask
from airfly.model.base import TaskTree, collect_taskpairs, collect_taskset
from airfly.utils import load_module_by_name

from .utils import InvalidModule, expand_sys_path, print_version


@click.command()
@click.option(
    "--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True
)
@click.option("--name", "-n", help="Assign DAG name")
@click.option("--modname", "-m", help="Input module name to generate airflow DAG")
@click.option(
    "--path",
    "-p",
    multiple=True,
    default=[os.getcwd()],
    help='Insert into "sys.path" to search modules, could assign with multiple values',
)
@click.option(
    "--exclude",
    "-e",
    help="Giving regex pattern to match the implementation to be excluded by its qualname",
)
def main(name, modname, path, exclude):
    with expand_sys_path(*path):
        try:
            module = load_module_by_name(modname)
        except Exception:
            raise InvalidModule(f'got: "{modname}"')

    taskset = set(collect_taskset(module, taskclass=AirflowTask))
    taskpairs = collect_taskpairs(taskset, taskclass=AirflowTask)

    tasktree = TaskTree(taskset=taskset, taskpairs=taskpairs)

    dag = AirflowDAG(name, tasktree)

    print(dag.render())
