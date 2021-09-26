def test_blacking():
    from airfly.utils import blacking

    assert blacking


def test_isorting():
    from airfly.utils import isorting

    assert isorting


def test_collect_objects():
    from airfly.utils import collect_objects

    assert collect_objects


def test_load_module_by_name():
    from airfly.utils import load_module_by_name

    assert load_module_by_name


def test_qualname():
    from airfly.utils import qualname

    assert qualname


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
