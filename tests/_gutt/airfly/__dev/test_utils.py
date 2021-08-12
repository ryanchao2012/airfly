def test_load_module_by_name():
    from airfly.__dev.utils import load_module_by_name

    assert load_module_by_name


def test_collect_classes_and_functions():
    from airfly.__dev.utils import collect_classes_and_functions

    assert collect_classes_and_functions


def test__escape_any_commandline_parser():
    from airfly.__dev.utils import _escape_any_commandline_parser

    assert _escape_any_commandline_parser


def test__collect_from_package():
    from airfly.__dev.utils import _collect_from_package

    assert _collect_from_package


def test__collect_from_module():
    from airfly.__dev.utils import _collect_from_module

    assert _collect_from_module


def test_makefile():
    from airfly.__dev.utils import makefile

    assert makefile


def test__writefile():
    from airfly.__dev.utils import _writefile

    assert _writefile
