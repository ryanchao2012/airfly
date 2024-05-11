import pytest


class TestInvalidModule:
    @classmethod
    def setup_class(cls):
        from airfly.cli.utils import InvalidModule

        assert InvalidModule

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


def test_convert_dag_params():
    from airfly.cli.utils import convert_dag_params

    assert convert_dag_params(None, None, None) is None

    value = "path:varname"
    param = convert_dag_params(None, None, value)

    assert isinstance(param, tuple)
    assert param[0] == "path"
    assert param[1] == "varname"


def test_expand_sys_path(mocker):
    from airfly.cli.utils import expand_sys_path

    mock_syspath = mocker.patch("sys.path")
    paths = ["path1", "path2"]
    with expand_sys_path(*paths):
        assert mock_syspath.insert.call_count == len(paths)

    assert mock_syspath.pop.call_count == len(paths)


def test_print_version(mocker):
    from airfly.cli.utils import print_version

    mock_click = mocker.patch("airfly.cli.utils.click")
    mock_ctx = mocker.MagicMock()
    mock_ctx.resilient_parsing = None

    print_version(mock_ctx, None, mocker.MagicMock())

    assert mock_click.echo.called
    assert mock_ctx.exit.called


def test_validate_includes():
    from airfly.cli.utils import validate_includes

    with pytest.raises(FileNotFoundError):
        validate_includes(None, None, ["non_existent_path"])
