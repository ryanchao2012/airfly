def test_foo():
    from airfly.lab.mod2.a import foo

    assert foo


class Testquery_user:
    @classmethod
    def setup_class(cls):
        from airfly.lab.mod2.a import query_user

        assert query_user

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testquery_log:
    @classmethod
    def setup_class(cls):
        from airfly.lab.mod2.a import query_log

        assert query_log

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testprocess_data:
    @classmethod
    def setup_class(cls):
        from airfly.lab.mod2.a import process_data

        assert process_data

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
