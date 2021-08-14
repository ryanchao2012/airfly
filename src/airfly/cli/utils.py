import sys
from contextlib import contextmanager

import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
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


class InvalidModule(Exception):
    pass
