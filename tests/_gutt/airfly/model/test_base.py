class TestTaskTree:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import TaskTree

        assert TaskTree

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__create_dag(self):
        pass


def test_collect_taskpairs():
    from airfly.model.base import collect_taskpairs

    assert collect_taskpairs


def test_collect_taskset():
    from airfly.model.base import collect_taskset

    assert collect_taskset


class TestBaseTask:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import BaseTask

        assert BaseTask

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestWorkflow:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import Workflow

        assert Workflow

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_to_source(self):
        pass

    def test_to_file(self):
        pass


class TestTaskPair:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import TaskPair

        assert TaskPair

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
