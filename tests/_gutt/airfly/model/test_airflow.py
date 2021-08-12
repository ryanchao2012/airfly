class TestAirflowTask:
    @classmethod
    def setup_class(cls):
        from airfly.model.airflow import AirflowTask

        assert AirflowTask

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__resolve_operator(self):
        pass

    def test__resolve_dependency_from_params(self):
        pass

    def test_collect_dep_stmts(self):
        pass

    def test_to_stmt(self):
        pass
