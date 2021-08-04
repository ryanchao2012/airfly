class TestWorkflow:
    @classmethod
    def setup_class(cls):
        from airfly.workflow.base import Workflow

        assert Workflow

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_populate(self):
        pass
