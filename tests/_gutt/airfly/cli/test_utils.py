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

    assert convert_dag_params


def test_expand_sys_path():
    from airfly.cli.utils import expand_sys_path

    assert expand_sys_path


def test_print_version():
    from airfly.cli.utils import print_version

    assert print_version


def test_should_exclude():
    from airfly.cli.utils import should_exclude

    assert should_exclude


def test_validate_includes():
    from airfly.cli.utils import validate_includes

    assert validate_includes
