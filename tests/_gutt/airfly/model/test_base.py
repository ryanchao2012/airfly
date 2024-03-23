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

    def test_roots(self):
        pass

    def test_leaves(self):
        pass

    def test_nodes(self):
        pass

    def test_edges(self):
        pass


def test_collect_taskpairs():
    from airfly.model.base import collect_taskpairs

    assert collect_taskpairs


def test_collect_taskset():
    from airfly.model.base import collect_taskset

    assert collect_taskset


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
