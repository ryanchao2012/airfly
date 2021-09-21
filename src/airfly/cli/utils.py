import os
import sys
from contextlib import contextmanager
from types import FunctionType
from typing import Optional, Union

import click
import regex as re
from airfly.utils import qualname


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    from airfly import __version__

    click.echo(f"Version: {__version__}")

    ctx.exit()


def should_exclude(
    obj: Union[FunctionType, type], pattern: Optional[str] = None, verbose: bool = True
):
    if pattern and isinstance(pattern, str):
        obj_name = qualname(obj)
        if re.search(pattern, obj_name):
            if verbose:
                click.secho("excluding ", err=True, nl=False, fg="bright_white")
                click.secho(obj_name, err=True, fg="bright_black")
            return True

    return False


@contextmanager
def expand_sys_path(*paths: str):

    num = len(paths)

    for p in paths[::-1]:
        if p and isinstance(p, str):

            sys.path.insert(0, p)

    yield

    for _ in range(num):
        sys.path.pop(0)


def validate_includes(ctx, param, value):
    if value:
        for inc in value:
            if not os.path.isfile(inc):
                raise FileNotFoundError(f"Invalid file, got: {inc}")

        return list(value)

    return value


def convert_dag_params(ctx, param, value):

    if not value:
        return (None, None)

    elif isinstance(value, tuple):
        return value

    try:
        pypath, _, varname = value.partition(":")
        return pypath, varname

    except ValueError:
        raise click.BadParameter("format must be '<python-file>:<variable>'")


class InvalidModule(Exception):
    pass
