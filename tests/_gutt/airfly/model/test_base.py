class TestTask:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import Task

        assert Task

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestTask_:
    @classmethod
    def setup_class(cls):
        from airfly.model.base import Task_

        assert Task_

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
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


def test_collect_taskset():
    from airfly.model.base import collect_taskset

    assert collect_taskset


def test_build_taskpairs():
    from airfly.model.base import build_taskpairs

    assert build_taskpairs
