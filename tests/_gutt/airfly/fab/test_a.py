class TestATask:
    @classmethod
    def setup_class(cls):
        from airfly.fab.a import ATask

        assert ATask

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestBTask:
    @classmethod
    def setup_class(cls):
        from airfly.fab.a import BTask

        assert BTask

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
