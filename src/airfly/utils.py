import importlib
import io
import os
import pathlib
import pkgutil
import subprocess as sp
import sys
import tempfile
from contextlib import contextmanager
from types import FunctionType, ModuleType
from typing import Callable, Generator, Union

import attr
import loguru

immutable = attr.s(auto_attribs=True, slots=True, frozen=True, kw_only=True)


def qualname(obj: Union[FunctionType, ModuleType, type], level: int = -1) -> str:
    """Return the qualname of a class, a function or a module.

    >>> class Foo:
    ...     pass

    >>> def bar():
    ...     pass

    >>> qualname(Foo)
    'airfly.utils.Foo'

    >>> qualname(bar)
    'airfly.utils.bar'
    """

    if isinstance(obj, FunctionType) or isinstance(obj, type):
        name = f"{obj.__module__}.{obj.__qualname__}"

    elif isinstance(obj, ModuleType):
        name = f"{obj.__name__}"

    else:
        name = ""

    return ".".join(name.split(".")[-level:]) if level > 0 else name


def issubclass_by_qualname(cls, class_or_tuple):
    mro = {qualname(o) for o in cls.mro()}

    if isinstance(class_or_tuple, type):
        class_or_tuple = (class_or_tuple,)

    for o in class_or_tuple:
        if qualname(o) in mro:
            return True

    return False


def blacking(source_code: str):

    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(source_code)
        fname = f.name

    with sp.Popen(["cat", fname], stdout=sp.PIPE) as p:
        cmd = [sys.executable, "-m", "black", "-q", "-"]
        out = sp.check_output(cmd, stdin=p.stdout)

    try:
        pathlib.Path(fname).unlink()

    except FileNotFoundError:
        pass

    return out.decode()


def isorting(source_code: str):

    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(source_code)
        fname = f.name

    with sp.Popen(["cat", fname], stdout=sp.PIPE) as p:
        cmd = [sys.executable, "-m", "isort", "--profile", "black", "-q", "-"]
        out = sp.check_output(cmd, stdin=p.stdout)

    try:
        pathlib.Path(fname).unlink()

    except FileNotFoundError:
        pass

    return out.decode()


def collect_objects(
    module: ModuleType,
    predicate: Callable[[Union[FunctionType, type]], bool] = lambda _: True,
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
            if predicate(obj):
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

    for _, name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):

        with _escape_any_commandline_parser():
            try:
                mod = importlib.import_module(name)

            except Exception as e:
                loguru.logger.warning(f"Ignore invalid module: '{name}'. Reason: {e}")
                continue

        for obj in _collect_from_module(mod):
            yield obj


def _collect_from_module(
    module: ModuleType,
) -> Generator[Union[FunctionType, type], None, None]:

    for key, obj in module.__dict__.items():

        try:
            if isinstance(obj, (type, FunctionType)):
                yield obj
        except Exception as err:
            loguru.logger.warning(f"Ignore invalid object: '{key}'. Reason: {err}")


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
