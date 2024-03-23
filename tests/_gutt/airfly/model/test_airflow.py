class TestDAGBuilder:
    @classmethod
    def setup_class(cls):
        from airfly.model.airflow import DAGBuilder

        assert DAGBuilder

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_to_module(self):
        pass

    def test_render(self):
        pass

    def test__build_includes(self):
        pass

    def test__build_header(self):
        pass

    def test__parse_dag_params_from_pyfile(self):
        pass

    def test__build_dag_context(self):
        pass

    def test__build_dag_body(self):
        pass

    def test__build_imports(self):
        pass

    def test__insert_from_pyfile(self):
        pass


class TestAirFly:
    @classmethod
    def setup_class(cls):
        from airfly.model.airflow import AirFly

        assert AirFly

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
