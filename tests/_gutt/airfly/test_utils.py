import pytest


@pytest.mark.parametrize(
    "src,exp",
    [
        (["", "", ""], ["\n"]),
        (
            ["def foo():", "    ", "    ", "    ", "    pass"],
            ["def foo():", "", "    pass", ""],
        ),
        (
            ["import os", "def foo():", "    pass"],
            ["import os", "", "", "def foo():", "    pass", ""],
        ),
    ],
)
def test_blacking(src, exp):
    from airfly.utils import blacking

    assert blacking("\n".join(src)) == "\n".join(exp)


@pytest.mark.parametrize(
    "src,exp",
    [
        (["import sys", "import os"], ["import os", "import sys", ""]),
        (["import airfly", "import os"], ["import os", "", "import airfly", ""]),
        (
            ["from airfly.utils import qualname", "import airfly"],
            ["import airfly", "from airfly.utils import qualname", ""],
        ),
        (
            ["from . import isorting", "import airfly"],
            ["import airfly", "", "from . import isorting", ""],
        ),
    ],
)
def test_isorting(src, exp):
    from airfly.utils import isorting

    assert isorting("\n".join(src)) == "\n".join(exp)


def test_collect_objects(mocker):

    mock_collect_from_package = mocker.patch("airfly.utils._collect_from_package")
    mock_collect_from_module = mocker.patch("airfly.utils._collect_from_module")
    import airfly
    from airfly import utils
    from airfly.utils import collect_objects

    _ = list(collect_objects(airfly))

    assert (
        mock_collect_from_package.call_count == 1
        and mock_collect_from_module.call_count == 0
    )

    mocker.resetall()

    _ = list(collect_objects(utils))
    assert (
        mock_collect_from_package.call_count == 0
        and mock_collect_from_module.call_count == 1
    )


def test_qualname():
    from airfly.utils import qualname

    assert qualname(qualname) == "airfly.utils.qualname"
    assert qualname(qualname, level=2) == "utils.qualname"
    assert qualname(qualname, level=100) == "airfly.utils.qualname"
    assert qualname(qualname, level=-1) == "airfly.utils.qualname"


def test__escape_any_commandline_parser():
    from airfly.utils import _escape_any_commandline_parser

    assert _escape_any_commandline_parser


def test__collect_from_package():
    from airfly.utils import _collect_from_package

    assert _collect_from_package


def test__collect_from_module():
    from airfly.utils import _collect_from_module

    assert _collect_from_module


def test_makefile():
    from airfly.utils import makefile

    assert makefile


def test__writefile():
    from airfly.utils import _writefile

    assert _writefile


def test_issubclass_by_qualname():
    from airfly.utils import issubclass_by_qualname

    class Foo: ...

    class Bar(Foo): ...

    class Buz: ...

    assert issubclass_by_qualname(Bar, Foo)
    assert not issubclass_by_qualname(Buz, Foo)
