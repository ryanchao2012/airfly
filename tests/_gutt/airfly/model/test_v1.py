import asttrs
import attr
import pytest

from airfly.utils import qualname


class TestLiteral:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import Literal

        cls.Literal = Literal

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        "expected", ["MyClass(*args, **kwargs)", "my_wrapper(some_function)"]
    )
    def test_repr(self, expected):

        assert repr(self.Literal(expected)) == expected

    def test__to_ast(self):

        assert self.Literal("any expression")._to_ast() == asttrs.Name(
            id="any expression", ctx=asttrs.Load()
        )

    def test__dep_ast(self):

        assert (
            #
            self.Literal("any expression", deps=self.Literal)._dep_ast()[0]
            == asttrs.ImportFrom(
                module=self.Literal.__module__, names=[asttrs.alias(name="Literal")]
            )
        )


class TestParam:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import Param

        cls.Param = Param

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        "obj,expected",
        [
            (123, asttrs.Constant(value=123)),
            ("abc", asttrs.Constant(value="abc")),
            (
                [123],
                asttrs.List(
                    elts=[asttrs.Constant(value=123)],
                    ctx=asttrs.Load(),
                ),
            ),
            (
                dict(abc=123),
                asttrs.Dict(
                    keys=[asttrs.Constant(value="abc")],
                    values=[asttrs.Constant(value=123)],
                ),
            ),
        ],
    )
    def test__target_ast(self, obj, expected):

        self.Param(obj)._target_ast() == expected

    def test__target_ast_other_cases(self):
        from airfly.model import Literal

        assert self.Param(self.Param)._target_ast() == asttrs.Name(
            id="Param", ctx=asttrs.Load()
        )

        assert self.Param([self.Param])._target_ast() == asttrs.List(
            elts=[asttrs.Name(id="Param", ctx=asttrs.Load())], ctx=asttrs.Load()
        )

        assert self.Param(self.setup_class)._target_ast() == asttrs.Name(
            id="TestParam.setup_class", ctx=asttrs.Load()
        )

        assert self.Param([self.setup_class])._target_ast() == asttrs.List(
            elts=[asttrs.Name(id="TestParam.setup_class", ctx=asttrs.Load())],
            ctx=asttrs.Load(),
        )

        # Literal cases
        assert self.Param(Literal("any expression"))._target_ast() == asttrs.Name(
            id="any expression", ctx=asttrs.Load()
        )

        with pytest.raises(TypeError):
            self.Param(lambda: True)._target_ast()

        with pytest.raises(TypeError):
            self.Param(object())._target_ast()

    @pytest.mark.parametrize(
        "obj", [123, "abc", [123], {"abc"}, dict(abc=123), object()]
    )
    def test__dep_ast(self, obj):

        assert self.Param(obj)._dep_ast() == []

    def test__dep_ast_other_cases(self):
        from airfly.model import Literal

        assert (
            self.Param(Literal("Literal('any expression')", deps=Literal))._dep_ast()
            == self.Param(Literal)._dep_ast()
        )

        assert (
            #
            self.Param(
                Literal(
                    "Literal('any expression')", deps=Literal("any import expression")
                )
            )._dep_ast()
            == asttrs.Name(id="any import expression", ctx=asttrs.Load())
        )

    def test__dep_ast_other_cases(self):

        assert self.Param(self.Param)._dep_ast()[0] == asttrs.ImportFrom(
            module=self.Param.__module__, names=[asttrs.alias(name=self.Param.__name__)]
        )

        assert self.Param(self.Param, alias="Param_1")._dep_ast()[
            0
        ] == asttrs.ImportFrom(
            module=self.Param.__module__,
            names=[asttrs.alias(name=self.Param.__name__, asname="Param_1")],
        )


class TestParamContext:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import ParamContext

        cls.ParamContext = ParamContext

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_get(self):

        assert self.ParamContext.get(self.ParamContext).target == self.ParamContext

    def test__get(self):

        ctx = self.ParamContext()
        par1 = ctx._get(self.ParamContext)

        key1 = qualname(self.ParamContext)
        assert key1 in ctx.params
        assert ctx.params[key1] == par1

        _ = ctx._get([self.ParamContext])
        assert len(ctx.params) == 1

        _ = ctx._get(dict(param_ctx=self.ParamContext))
        assert len(ctx.params) == 1

    def test__find_alias_without_conflict(self):

        conflicts = {"key": 0}
        ctx = self.ParamContext()
        ctx.conflicts = conflicts

        assert ctx._find_alias_without_conflict("key") == "key_1"
        assert conflicts["key"] == 1

        conflicts["key_2"] = 0
        assert ctx._find_alias_without_conflict("key") == "key_2_1"
        assert conflicts["key_2"] == 1


class TestTaskAttribute:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import TaskAttribute

        assert TaskAttribute

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


class TestTask:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import Task

        cls.Task = Task

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__get_taskid(self):

        assert self.Task._get_taskid(self.Task) == qualname(self.Task)

        class MyTask:
            @classmethod
            def _get_taskid(cls):
                return "my_task"

        assert self.Task._get_taskid(MyTask) == "my_task"

    def test__get_attributes(self):
        from airfly.model.v1 import TaskAttribute
        from airfly.utils import immutable

        # Base case
        class Task1: ...

        class Task2: ...

        class Task3: ...

        task_attr = immutable(TaskAttribute)(
            op_class="MyOperator",
            op_params=dict(abc=123),
            upstream=[Task1, Task2],
            downstream=Task3,
        )

        class Task4:
            op_class = task_attr.op_class

            @property
            def op_params(self):
                return task_attr.op_params

            @property
            def upstream(self):
                return task_attr.upstream

            downstream = task_attr.downstream

        cache = self.Task._get_attributes(Task4)

        assert self.Task._get_attributes(Task4) is cache

        for a in attr.fields(task_attr.__class__):
            assert getattr(cache, a.name) == getattr(task_attr, a.name)

        # Test attribute inherience

        parent_module = "parent_module"
        parent_params = None
        parent_upstream = Task1
        parent_downstream = None
        child_module = "child_module"
        child_params = dict(child=2)
        child_upstream = Task2
        child_downstream = Task3

        class Task5:
            op_class = "ParamOperator"

            # defined class-var
            op_module = parent_module

            # None class-var
            op_params = parent_params

            # defined property
            @property
            def upstream(self):
                return parent_upstream

            # None property
            @property
            def downstream(self):
                return parent_downstream

        class Task6(Task5):
            """Implement nothing
            Expect inherient attributes from parent for all cases.
            """

            ...

        attr6 = self.Task._get_attributes(Task6)
        assert attr6.op_module == parent_module
        assert attr6.op_params is parent_params is None
        assert attr6.upstream == parent_upstream
        assert attr6.downstream is parent_downstream is None

        class Task7(Task5):
            """Define(override) all attributes with class-var"""

            op_module = child_module
            op_params = child_params
            upstream = child_upstream
            downstream = child_downstream

        attr7 = self.Task._get_attributes(Task7)
        assert attr7.op_module == child_module
        assert attr7.op_params == child_params
        assert attr7.upstream == child_upstream
        assert attr7.downstream == child_downstream

        class Task8(Task5):
            """Reset defined attributs to None with class-var"""

            op_module = None
            upstream = None

        attr8 = self.Task._get_attributes(Task8)
        assert attr8.op_module is None
        assert attr8.upstream is None

        class Task9(Task5):
            """Define(override) all attributes with property"""

            @property
            def op_module(self):
                return child_module

            @property
            def op_params(self):
                return child_params

            @property
            def upstream(self):
                return child_upstream

            @property
            def downstream(self):
                return child_downstream

        attr9 = self.Task._get_attributes(Task9)
        assert attr9.op_module == child_module
        assert attr9.op_params == child_params
        assert attr9.upstream == child_upstream
        assert attr9.downstream == child_downstream

        class Task10(Task5):
            """Reset defined attributs to None with property"""

            @property
            def op_module(self):
                return None

            @property
            def upstream(self):
                return None

        attr10 = self.Task._get_attributes(Task10)

        assert attr10.op_module is None
        assert attr10.upstream is None

    def test__to_varname(self):
        assert self.Task._to_varname(self.Task) == qualname(self.Task).replace(".", "_")

        class MyTask:
            @classmethod
            def _to_varname(cls):
                return "my_var"

        assert self.Task._to_varname(MyTask) == "my_var"

    def test__collect_dep_ast(self):

        class Task1:
            op_class = "BashOperator"

        class Task2:
            op_class = "BashOperator"
            op_params = dict(my_dep=self.Task)

        assert self.Task._collect_dep_ast(Task1)[0] == asttrs.ImportFrom(
            module="airflow.operators.bash",
            names=[asttrs.alias(name="BashOperator")],
        )

        assert asttrs.ImportFrom(
            module="airfly.model.v1", names=[asttrs.alias(name="Task")]
        ) in self.Task._collect_dep_ast(Task2)

    def test__to_ast(self):

        class Task:
            op_class = "BashOperator"

        assert isinstance(self.Task._to_ast(Task), asttrs.Assign)

    def test__resolve_operator(self):
        from airfly._vendor.airflow.operators.bash import BashOperator
        from airfly._vendor.airflow.providers.google.cloud.operators.dataproc import (
            DataprocCreateClusterOperator,
        )

        class Task1:
            op_class = "BashOperator"

        class Task2:
            op_class = BashOperator

        class Task3:
            op_class = DataprocCreateClusterOperator

        class Task4:
            op_class = "NonExistentOperator"

        class MyOperator: ...

        class Task5:
            op_class = MyOperator

        class Task6:
            op_class = "DataprocCreateClusterOperator"

        class Task7:
            op_class = "DataprocCreateClusterOperator"
            op_module = "google"

        assert self.Task._resolve_operator(Task1) == BashOperator
        assert self.Task._resolve_operator(Task2) == BashOperator
        assert self.Task._resolve_operator(Task3) == DataprocCreateClusterOperator

        with pytest.raises(ValueError):
            self.Task._resolve_operator(Task4)

        with pytest.raises(TypeError):
            self.Task._resolve_operator(Task5)

        with pytest.raises(ValueError):
            self.Task._resolve_operator(Task6)

        assert self.Task._resolve_operator(Task7) == DataprocCreateClusterOperator

    def test__collect_op_annotations(self):
        pass

    @pytest.mark.parametrize(
        "op_name",
        ["BashOperator", "PythonOperator", "KubernetesPodOperator"],
    )
    def test__is_builtin_op(self, op_name):

        class Task(self.Task):
            op_class = op_name

        op = self.Task._resolve_operator(Task)

        assert self.Task._is_builtin_op(op)

    def test__is_private_op(self, mocker):

        assert not self.Task._is_private_op(mocker.MagicMock())


class TestAirFly:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import AirFly

        assert AirFly

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
        from airfly.model.v1 import TaskPair

        cls.TaskPair = TaskPair

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__to_ast(self, mocker):

        mock_Task = mocker.patch("airfly.model.v1.Task")

        class Task1: ...

        class Task2: ...

        pair = self.TaskPair(up=Task1, down=Task2)

        _ast = pair._to_ast()

        assert isinstance(_ast, asttrs.Expr)
        assert isinstance(_ast.value, asttrs.BinOp)
        assert isinstance(_ast.value.op, asttrs.RShift)

        assert mock_Task._to_varname.call_count == 2


class TestTaskTree:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import TaskTree

        cls.TaskTree = TaskTree

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__create_dag(self):
        pass

    def test_from_module(self):
        pass

    def test__should_exclude(self):

        class Foo: ...

        assert self.TaskTree._should_exclude(Foo, "Foo")
        assert self.TaskTree._should_exclude(Foo, "_gutt")
        assert not self.TaskTree._should_exclude(Foo, "Bar")

    def test__collect_taskclass(self):
        pass

    def test__collect_taskpairs(self):

        class Task:
            op_class = "BashOperator"

        class Task1(Task): ...

        class Task2(Task):
            upstream = Task1

        class Task3(Task):
            downstream = Task2

        class Task4(Task):
            upstream = [Task1, Task2]
            downstream = Task3

        assert len(list(self.TaskTree._collect_taskpairs({Task4}, Task))) == 3
        assert len(list(self.TaskTree._collect_taskpairs({Task1, Task4}, Task))) == 3
        assert len(list(self.TaskTree._collect_taskpairs({Task3, Task4}, Task))) == 4
        assert (
            len(list(self.TaskTree._collect_taskpairs({Task2, Task3, Task4}, Task)))
            == 5
        )

    def test_to_dag(self):
        pass

    def test__to_ast(self):
        pass

    def test__build_header(self):
        import airfly

        tree = self.TaskTree(taskset=set(), taskpairs=set())
        header = tree._build_header()[0]

        assert isinstance(header, asttrs.Comment)
        assert airfly.__version__ in header.body

    def test__build_imports(self):

        tree = self.TaskTree(taskset={}, taskpairs=set())
        _imports = tree._build_imports()

        assert (
            asttrs.ImportFrom(module="airflow.models", names=[asttrs.alias(name="DAG")])
            in _imports
        )

    def test__build_includes(self, mocker):
        mock_insert_from_pyfile = mocker.patch(
            "airfly.model.v1.TaskTree._insert_from_pyfile"
        )
        tree = self.TaskTree(taskset=set(), taskpairs=set())

        assert tree._build_includes() == []

        includes = ["path1", "path2", "path3"]
        _ = tree._build_includes(includes)

        assert mock_insert_from_pyfile.call_count == len(includes)

    def test__insert_from_pyfile(self):
        pass

    def test__build_dag_context(self, mocker):
        mock_build_dag_body = mocker.patch(
            "airfly.model.v1.TaskTree._build_dag_body", return_value=[asttrs.Pass()]
        )

        tree = self.TaskTree(taskset=set(), taskpairs=set())

        dag_name = "my_dag"
        dag_params = ("a_python_file.py", "a_var_name")
        _ctx_mgr = tree._build_dag_context(dag_name, dag_params)[0]

        assert mock_build_dag_body.call_count == 1
        assert isinstance(_ctx_mgr, asttrs.With)

        _withitem = _ctx_mgr.items[0]
        assert isinstance(_withitem.context_expr, asttrs.Call)

        _call = _withitem.context_expr
        assert isinstance(_call.args[0], asttrs.Constant)
        assert _call.args[0].value == dag_name

        assert isinstance(_call.keywords[0].value, asttrs.Name)
        assert _call.keywords[0].value.id == dag_params[1]

    def test__build_dag_body(self, mocker):
        mock_TaskPair = mocker.patch("airfly.model.v1.TaskPair")
        mock_Task = mocker.patch("airfly.model.v1.Task")

        class Task1: ...

        class Task2: ...

        class Task3: ...

        taskset = {Task1, Task2, Task3}
        taskpairs = {
            mock_TaskPair(up=Task1, down=Task2),
            mock_TaskPair(up=Task1, down=Task3),
            mock_TaskPair(up=Task2, down=Task3),
        }

        empty_tree = self.TaskTree(taskset=set(), taskpairs=set())

        body = empty_tree._build_dag_body()
        assert len(body) == 1 and body[0] == asttrs.Pass()

        tree = self.TaskTree(taskset=taskset, taskpairs=taskpairs)

        _ = tree._build_dag_body()

        assert mock_Task._to_ast.call_count == len(taskset)
        assert mock_Task._collect_dep_ast.call_count == len(taskset)

        for pair in taskpairs:
            assert pair._to_ast.call_count == 1

    def test__build_task_group(self):
        pass


class TestTaskGroup:
    @classmethod
    def setup_class(cls):
        from airfly.model.v1 import TaskGroup

        assert TaskGroup

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test__to_ast(self):
        pass

    def test__to_varname(self):
        pass
