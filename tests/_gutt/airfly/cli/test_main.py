import pytest
from click.testing import CliRunner

from airfly.cli.utils import InvalidModule


@pytest.fixture()
def runner():
    return CliRunner()


def test_main(mocker, runner):
    from airfly.cli.main import main

    mock_tree = mocker.MagicMock()
    mock_TaskTree = mocker.patch("airfly.cli.main.TaskTree")

    mock_TaskTree.from_module.return_value = mock_tree

    result = runner.invoke(main, ["--modname", "not_existent_module"])
    assert result.exit_code == 1
    assert isinstance(result.exception, InvalidModule)

    result = runner.invoke(main, ["--modname", "airfly"])
    assert result.exit_code == 0
    assert mock_TaskTree.from_module.called
    assert mock_tree.to_dag.called
