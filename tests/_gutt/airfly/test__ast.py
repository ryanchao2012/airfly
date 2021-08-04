class Test_AST:
    @classmethod
    def setup_class(cls):
        from airfly._ast import _AST

        assert _AST

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestAST:
    @classmethod
    def setup_class(cls):
        from airfly._ast import AST

        assert AST

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_render(self):
        pass

    def test_get_ast_type(self):
        pass

    def test_dump(self):
        pass


class TestTypeIgnore:
    @classmethod
    def setup_class(cls):
        from airfly._ast import TypeIgnore

        assert TypeIgnore

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testalias:
    @classmethod
    def setup_class(cls):
        from airfly._ast import alias

        assert alias

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testexpr_context:
    @classmethod
    def setup_class(cls):
        from airfly._ast import expr_context

        assert expr_context

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestLoad:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Load

        assert Load

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestStore:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Store

        assert Store

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestDel:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Del

        assert Del

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testarg:
    @classmethod
    def setup_class(cls):
        from airfly._ast import arg

        assert arg

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testexpr:
    @classmethod
    def setup_class(cls):
        from airfly._ast import expr

        assert expr

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestName:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Name

        assert Name

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testkeyword:
    @classmethod
    def setup_class(cls):
        from airfly._ast import keyword

        assert keyword

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestCall:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Call

        assert Call

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testarguments:
    @classmethod
    def setup_class(cls):
        from airfly._ast import arguments

        assert arguments

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestConstant:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Constant

        assert Constant

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Teststmt:
    @classmethod
    def setup_class(cls):
        from airfly._ast import stmt

        assert stmt

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestExpr:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Expr

        assert Expr

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestAssign:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Assign

        assert Assign

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestImport:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Import

        assert Import

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestImportFrom:
    @classmethod
    def setup_class(cls):
        from airfly._ast import ImportFrom

        assert ImportFrom

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestPass:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Pass

        assert Pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestFunctionDef:
    @classmethod
    def setup_class(cls):
        from airfly._ast import FunctionDef

        assert FunctionDef

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestIf:
    @classmethod
    def setup_class(cls):
        from airfly._ast import If

        assert If

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class Testwithitem:
    @classmethod
    def setup_class(cls):
        from airfly._ast import withitem

        assert withitem

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestWith:
    @classmethod
    def setup_class(cls):
        from airfly._ast import With

        assert With

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestModule:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Module

        assert Module

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestClassDefinition:
    @classmethod
    def setup_class(cls):
        from airfly._ast import ClassDefinition

        assert ClassDefinition

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestSerializable:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Serializable

        assert Serializable

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_to_dict(self):
        pass

    def test_from_dict(self):
        pass

    def test_from_json(self):
        pass

    def test_to_json(self):
        pass

    def test_evolve(self):
        pass

    def test_mutate_from_other(self):
        pass


class Testslice:
    @classmethod
    def setup_class(cls):
        from airfly._ast import slice

        assert slice

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestIndex:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Index

        assert Index

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestSubscript:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Subscript

        assert Subscript

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestComment:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Comment

        assert Comment

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_get_ast_type(self):
        pass


class TestClassDef:
    @classmethod
    def setup_class(cls):
        from airfly._ast import ClassDef

        assert ClassDef

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestAnnAssign:
    @classmethod
    def setup_class(cls):
        from airfly._ast import AnnAssign

        assert AnnAssign

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestCode:
    @classmethod
    def setup_class(cls):
        from airfly._ast import Code

        assert Code

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
