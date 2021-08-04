class TestAirflowWorkflow:
    @classmethod
    def setup_class(cls):
        from airfly.workflow._airflow import AirflowWorkflow

        assert AirflowWorkflow

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
