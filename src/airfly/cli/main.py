import os

import click

from airfly.model import TaskTree
from airfly.utils import load_module_by_name

from .utils import (
    InvalidModule,
    convert_dag_params,
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
def main(name, modname, path, exclude_pattern, includes, dag_params):

    with expand_sys_path(*path):
        try:
            module = load_module_by_name(modname)
        except Exception:
            raise InvalidModule(f'got: "{modname}"')

    name = name or f"{modname}_dag"

    if dag_params[0]:
        if includes:
            includes.append(dag_params[0])
        else:
            includes = [dag_params[0]]

    tree = TaskTree.from_module(module, exclude_pattern=exclude_pattern)

    print(tree.to_dag(name, includes=includes, dag_params=dag_params), end="")
