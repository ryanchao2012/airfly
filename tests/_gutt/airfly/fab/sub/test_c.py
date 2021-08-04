class TestCTask:
    @classmethod
    def setup_class(cls):
        from airfly.fab.sub.c import CTask

        assert CTask

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
