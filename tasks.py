import configparser
import inspect
import os
import time
from pathlib import Path
from types import ModuleType

import click
import regex as re
from airflow.models.baseoperator import BaseOperator
from invoke import task

import airfly as package
from airfly._ast import (
    AnnAssign,
    ClassDef,
    Comment,
    Constant,
    ImportFrom,
    Module,
    Name,
    Pass,
    alias,
)
from airfly.utils import collect_objects, load_module_by_name, makefile, qualname

PACKAGE_NAME = package.__name__
# PACKAGE_VERSION = package.__version__


@task(
    help=dict(
        tomlfile="Iput config file to load, default: pyproject.toml",
        metafile=f"Output python file to write meta data, default: src/{PACKAGE_NAME}/_meta.py",
    )
)
def sync_meta(c, tomlfile=None, metafile=None):
    """Sync project metadata with pyproject.toml"""

    project_root = os.path.dirname(__file__)

    tomlfile = tomlfile or os.path.join(project_root, "pyproject.toml")
    parser = configparser.ConfigParser()
    parser.read(tomlfile)

    meta: dict = parser._sections["tool.poetry"]
    metafile = metafile or os.path.join(project_root, "src", PACKAGE_NAME, "_meta.py")

    header = '# NOTE: This file is auto-generated by "inv sync-meta"\n\n'
    content = header + "\n".join(f"{k} = {v}" for k, v in meta.items()) + "\n"

    with open(metafile, "w") as f:
        f.write(content)


def _collect_operators(module: ModuleType, exclude=None, sleep_interval=0.01):
    impls = []
    items = 0
    should_nl = True

    for obj in collect_objects(module):
        if not (isinstance(obj, type) and issubclass(obj, BaseOperator)):
            continue

        obj_name = qualname(obj)

        if isinstance(exclude, str) and re.search(exclude, obj_name):
            if should_nl:
                click.echo()
                should_nl = False
            click.secho("excluding ", nl=False, fg="bright_white")
            click.secho(obj_name, fg="bright_black")

            continue

        if obj not in impls:
            items += 1
            impls.append(obj)
            click.echo("\033[K", nl=False)
            click.secho(f"collecting {items} items: ", nl=False, fg="bright_white")
            click.secho(f"{obj_name}\r", nl=False, fg="bright_cyan")
            time.sleep(sleep_interval)
            should_nl = True

    click.echo()

    return impls


@task()
def collect_airflow(c, output=f"src/{PACKAGE_NAME}/_vendor"):

    modname = "airflow"

    module = load_module_by_name(modname)

    impls = _collect_operators(module)

    namespace = re.sub(r"^src\.", "", output.replace("/", "."))

    scopes = {}

    def collect_code(cls):

        for parent in cls.__bases__:
            if parent is object:
                continue

            collect_code(parent)

        mod = ".".join([namespace, cls.__module__])
        name = cls.__name__

        if mod not in scopes:
            scopes[mod] = {}

        if name not in scopes[mod]:

            bases = []

            for b in cls.__bases__:
                if b is not object:
                    bname = b.__name__
                    bmod = ".".join([namespace, b.__module__])
                    importfrom_ = ImportFrom(module=bmod, names=[alias(name=bname)])
                    id_ = f"Import{bname}"

                    if (id_ not in scopes[mod]) and bmod != mod:
                        scopes[mod].update({id_: importfrom_})

                    bases.append(bname)

            signature = inspect.signature(cls)
            params = signature.parameters
            body = []

            for k, v in params.items():

                anno = v.annotation
                if isinstance(anno, type):
                    typename = qualname(anno, level=1)

                elif hasattr(anno, "__module__") and anno.__module__ == "typing":
                    typename = str(anno)

                else:
                    raise TypeError(f"got: {anno}")

                if v.kind not in [
                    inspect._ParameterKind.VAR_KEYWORD,
                    inspect._ParameterKind.VAR_POSITIONAL,
                ]:

                    body.append(
                        AnnAssign(
                            target=Name(id=k),
                            annotation=Constant(value=typename),
                            # TODO: assign defaults
                            # value=(
                            #     Constant(value=v.default)
                            #     if v.default != inspect._empty
                            #     else None
                            # ),
                        )
                    )

            clsdef = ClassDef(
                name=name,
                bases=[Name(id=p) for p in bases],
                body=body or [Pass()],
            )

            scopes[mod].update({name: clsdef})

    for im in impls:
        collect_code(im)

    for dst_module, items in scopes.items():

        dstfile = f'src/{dst_module.replace(".", "/")}.py'

        makefile(dstfile)

        comment = Comment(body="Auto generated by 'inv collect-airflow'")

        body = sorted(
            [v for _, v in items.items()],
            key=lambda el: (
                "_" if type(el).__name__.find("Import") else type(el).__name__
            ),
        )

        module_ = Module(body=[comment] + body)

        click.secho("generating code into: ", nl=False, fg="bright_white")
        click.secho(f"{dstfile}\r", fg="bright_cyan")

        module_.dump(dstfile, formatted=True)

    output_root = Path(output)
    paths = {output_root}
    for path in output_root.glob("**/*.py"):
        if path.name == "__init__.py":
            continue

        parent = path.parent

        while parent > output_root:

            if not parent.joinpath("__init__.py").exists():
                paths.add(parent)

            parent = parent.parent

    for p in paths:
        makefile(os.path.join(str(p), "__init__.py"))
