import ast
import json
from typing import Any, Dict, List, Optional, Tuple, Type

import astor
import attr
import cattr

from airfly.utils import blacking, isorting

immutable = attr.s(auto_attribs=True, slots=True, frozen=True, kw_only=True)


class Serializable:
    @classmethod
    def to_dict(self, recurse=True, **kwargs):
        return attr.asdict(self, recurse=recurse, **kwargs)

    @classmethod
    def from_dict(cls, data: Dict):
        return cattr.structure_attrs_fromdict(data, cls)

    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))

    def to_json(self, ensure_ascii=False, **kwargs):
        return json.dumps(self.to_dict(), ensure_ascii=ensure_ascii, **kwargs)

    def evolve(self, **kwargs):
        return attr.evolve(self, **kwargs)

    def mutate_from_other(self, other: "Serializable", excludes=[]):
        valid_fields = [
            f1.name
            for f1 in attr.fields(other.__class__)
            if (getattr(other, f1.name, None) is not None)
            and (f1.name not in excludes)
            and (f1.name in [f2.name for f2 in attr.fields(self.__class__)])
        ]

        data = other.to_dict(filter=lambda att, value: att.name in valid_fields)

        return self.evolve(**data)


class _AST(Serializable):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return type(self).__name__


@immutable
class AST(_AST):
    @classmethod
    def get_ast_type(cls) -> Type[ast.AST]:
        return getattr(ast, cls.__name__)

    @property
    def ast(self) -> ast.AST:
        cls = type(self)
        fields: Tuple[attr.Attribute, ...] = (
            attr.fields(cls) if attr.has(cls) else tuple()
        )

        ast_type = self.get_ast_type()

        ast_fields: Tuple[str, ...] = ast_type._fields

        kwargs = {}

        for fd in fields:
            _name = fd.name
            if _name in ast_fields:

                value = getattr(self, _name)

                if isinstance(value, List):
                    value = [v.ast if isinstance(v, _AST) else v for v in value]
                else:
                    value = value.ast if isinstance(value, _AST) else value

                kwargs.update({_name: value})

        return ast_type(**kwargs)

    def render(self) -> str:

        return astor.to_source(self.ast)

    def dump(self, filepath: str, formatted: bool = False) -> Any:

        code = self.render()

        if formatted:
            code = blacking(isorting(code))

        with open(filepath, "w") as f:
            f.write(code)


@immutable
class TypeIgnore(AST):
    lineno: int
    tag: str


@immutable
class alias(AST):
    name: str
    asname: Optional[str] = None


class expr_context(AST):
    pass


class Load(expr_context):
    pass


class Store(expr_context):
    pass


class Del(expr_context):
    pass


@immutable
class arg(AST):
    arg: str
    annotation: Optional[str] = None
    type_comment: Optional[str] = None


class expr(AST):
    pass


@immutable
class Name(expr):
    id: str
    ctx: expr_context = Load()


@immutable
class keyword(AST):
    arg: str
    value: expr


class slice(AST):
    pass


@immutable
class Index(slice):
    value: expr


@immutable
class Call(expr):
    func: expr
    args: List[expr] = attr.ib(factory=list)
    keywords: List[keyword] = attr.ib(factory=list)


@immutable
class arguments(AST):

    posonlyargs: List[arg] = attr.ib(factory=list)
    args: List[arg] = attr.ib(factory=list)
    vararg: Optional[arg] = None
    kwonlyargs: List[arg] = attr.ib(factory=list)
    kw_defaults: List[expr] = attr.ib(factory=list)
    kwarg: Optional[arg] = None
    defaults: List[expr] = attr.ib(factory=list)


@immutable
class Constant(expr):
    value: str
    kind: Optional[str] = None


@immutable
class Subscript(expr):
    value: expr
    slice: expr
    ctx: expr_context = Load()


class stmt(AST):
    pass


@immutable
class Expr(stmt):
    value: expr


@immutable
class Comment(stmt):

    body: str

    @classmethod
    def get_ast_type(cls) -> Type[ast.AST]:
        return ast.Expr

    @property
    def ast(self) -> ast.AST:

        body: str = self.body.strip()

        cmt = body if body.startswith("#") else f"# {body}"

        return ast.Expr(value=ast.Name(id=cmt))


@immutable
class Assign(stmt):
    targets: List[expr]
    value: expr
    type_comment: Optional[str] = None


class Pass(stmt):
    pass


@immutable
class FunctionDef(stmt):
    name: str
    args: arguments
    body: List[stmt] = attr.ib(default=[Pass()])
    decorator_list: List[expr] = attr.ib(factory=list)
    returns: Optional[expr] = None
    type_comment: Optional[str] = None


@immutable
class withitem(AST):
    context_expr: expr
    optional_vars: Optional[expr] = None


@immutable
class With(stmt):
    items: List[withitem]
    body: List[stmt] = attr.ib(default=[Pass()])
    type_comment: Optional[str] = None


@immutable
class Module(AST):
    body: List[stmt] = attr.ib(factory=list)
    type_ignores: List[TypeIgnore] = attr.ib(factory=list)


@immutable
class ClassDef(stmt):
    name: str
    bases: List[expr] = attr.ib(factory=list)
    keywords: List[keyword] = attr.ib(factory=list)
    body: List[stmt] = attr.ib(default=[Pass()])
    decorator_list: List[expr] = attr.ib(factory=list)


@immutable
class AnnAssign(stmt):
    target: expr
    annotation: expr
    value: Optional[expr] = None
    simple: int = 1


@immutable
class Code(Serializable):

    modname: str
    module: Module = Module(body=[])


@immutable
class Import(stmt):
    names: List[alias] = attr.ib(factory=list)


@immutable
class ImportFrom(stmt):
    module: str
    names: List[alias] = attr.ib(factory=list)
    level: int = 0


class operator(AST):
    pass


class RShift(operator):
    pass


@immutable
class BinOp(expr):
    left: expr
    op: operator
    right: expr
