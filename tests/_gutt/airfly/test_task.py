class TestTask:
    @classmethod
    def setup_class(cls):
        from airfly.task import Task

        assert Task

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_run(self):
        pass


def test_make_task():
    from airfly.task import make_task

    assert make_task


def test_is_taskclass():
    from airfly.task import is_taskclass

    assert is_taskclass


def test_equipped_task():
    from airfly.task import equipped_task

    assert equipped_task


def test_collect_taskclass_from_module():
    from airfly.task import collect_taskclass_from_module

    assert collect_taskclass_from_module


class TestTaskPair:
    @classmethod
    def setup_class(cls):
        from airfly.task import TaskPair

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
        from airfly.task import TaskTree

        assert TaskTree

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_traverse(self):
        pass

    def test_pairs(self):
        pass
