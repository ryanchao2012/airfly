class TestTemplate:
    @classmethod
    def setup_class(cls):
        from airfly.workflow.template import Template

        assert Template

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_render(self):
        pass
