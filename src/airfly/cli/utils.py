import os
import sys
from contextlib import contextmanager

import click


def print_version(ctx, param, value):
    if (not value) or ctx.resilient_parsing:
        return

    from airfly import __version__

    click.echo(f"Version: {__version__}")

    ctx.exit()


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
        return None

    elif isinstance(value, tuple):
        return value

    try:
        pypath, _, varname = value.partition(":")
        return pypath, varname

    except ValueError:
        raise click.BadParameter("format must be '<python-file>:<variable>'")


def convert_task_group(ctx, param, value):

    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        return value == 1

    if isinstance(value, str):
        return value.lower() == "true" or value == "1"

    return False
