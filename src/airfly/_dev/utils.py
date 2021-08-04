import io
import os
import pkgutil
import sys
from contextlib import contextmanager
from importlib._bootstrap_external import SourceFileLoader
from types import FunctionType, ModuleType
from typing import Generator, Union

from airfly.utils import qualname


def load_module_by_name(modname: str) -> ModuleType:
    loader: SourceFileLoader = pkgutil.get_loader(modname)
    return loader.load_module(modname)


def collect_classes_and_functions(
    module: ModuleType,
) -> Generator[Union[FunctionType, type], None, None]:

    modname = qualname(module)
    cached = set()

    impls = (
        _collect_from_package(module)
        if hasattr(
            module, "__path__"
        )  # By definition, if a module has a __path__ attribute, it is a package.
        else _collect_from_module(module)
    )

    for obj in impls:
        name = qualname(obj)
        if obj.__module__.startswith(modname) and (name not in cached):
            cached.add(name)
            yield obj


@contextmanager
def _escape_any_commandline_parser():

    argv = sys.argv
    stdout = sys.stdout
    stderr = sys.stderr

    sys.argv = [""]
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    yield

    sys.argv = argv
    sys.stdout = stdout
    sys.stderr = stderr


def _collect_from_package(
    package: ModuleType,
) -> Generator[Union[FunctionType, type], None, None]:

    for obj in _collect_from_module(package):
        yield obj

    for finder, name, _ in pkgutil.walk_packages(
        package.__path__, package.__name__ + "."
    ):

        with _escape_any_commandline_parser():
            try:
                mod = finder.find_module(name).load_module(name)

            except BaseException:
                continue

        for obj in _collect_from_module(mod):

            yield obj


def _collect_from_module(
    module: ModuleType,
) -> Generator[Union[FunctionType, type], None, None]:
    for _, obj in module.__dict__.items():
        if isinstance(obj, (type, FunctionType)):

            yield obj


def makefile(fullpath: str, content: Union[str, bytes] = "", overwrite: bool = False):

    if not os.path.isfile(fullpath):

        dirpath = os.path.dirname(fullpath)

        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)

        _writefile(fullpath, content)

    elif overwrite:

        _writefile(fullpath, content)


def _writefile(fullpath: str, content: Union[str, bytes] = ""):

    if not isinstance(content, (str, bytes)):
        raise TypeError(f"content must be str or bytes, got: {type(content)}")

    with open(fullpath, "wb" if isinstance(content, bytes) else "w") as f:
        f.write(content)
