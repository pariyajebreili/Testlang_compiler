from anytree import NodeMixin
import uuid


class ASTNode(NodeMixin):  
    def __init__(self, name, id, children=None):
        self.name = name
        self.id = id
        if children:
            self.children = children



class ASTUtil(object):
    @staticmethod
    def prog_node1(func, prog):
        id = uuid.uuid4()
        children = [func]
        if prog:
            try:
                children.append(ASTUtil.prog_node(prog[1]["ast"], prog[2]["ast"]))
            except:
                children.append(ASTUtil.prog_node(prog[1]["ast"]))
        node = ASTNode("prgram", id, children)
        return node
    


class Node(object):
    def accept(self, visitor, table = None):
        return visitor.visit(self)
    def setParent(self, parent):
        self.parent = parent


class Prog1(Node):
    def __init__(self, func, lineno):
        self.lineno = lineno
        self.func = func
        self.children = ()


class Prog2(Node):
    def __init__(self, func, prog, lineno):
        self.lineno = lineno
        self.func = func
        self.prog = prog
        self.children = (func, prog,)



class Func(Node):
    def __init__(self, type, iden , flist, body, lineno):
        self.lineno = lineno
        self.type = type
        self.iden = iden
        self.flist = flist
        self.body = body
        self.children = (type, iden , flist, body,)


class Body1(Node):
    def __init__(self, stmt, lineno):
        self.lineno = lineno
        self.stmt = stmt
        self.children = (stmt,)


class Body2(Node):
    def __init__(self, stmt, body, lineno):
        self.lineno = lineno
        self.stmt = stmt
        self.body = body
        self.children = (stmt, body,)


class Stmt1(Node):
    def __init__(self, expr, lineno):
        self.lineno = lineno
        self.expr = expr
        self.children = (expr,)



class Stmt2(Node):
    def __init__(self, defvar, lineno):
        self.lineno = lineno
        self.defvar = defvar
        self.children = (defvar,)



class Stmt3(Node):
    def __init__(self, expr, stmt, else_choice, lineno):
        self.lineno = lineno
        self.expr = expr
        self.stmt = stmt
        self.else_choice = else_choice
        self.children = (expr, stmt, else_choice,)


class Stmt4(Node):
    def __init__(self, func, lineno):
        self.lineno = lineno
        self.func = func
        self.children = (func,)


class Stmt5(Node):
    def __init__(self, iden1, oper, expr1, expr2, stmt, lineno):
        self.lineno = lineno
        self.iden1 = iden1
        self.oper = oper
        self.expr1 = expr1
        self.expr2 = expr2
        self.stmt = stmt
        self.children = (iden1, expr1, expr2, stmt,)


class Stmt6(Node):
    def __init__(self, expr, lineno):
        self.lineno = lineno
        self.expr = expr
        self.children = (expr,)

class Stmt7(Node):
    def __init__(self, body, lineno):
        self.lineno = lineno
        self.body = body
        self.children = (body,)


class Stmt8(Node):
    def __init__(self, expr, stmt, lineno):
        self.lineno = lineno
        self.expr = expr
        self.stmt = stmt
        self.children = (expr, stmt,)



class Stmt9(Node):
    def __init__(self, defvar, lineno):
        self.lineno = lineno
        self.defvar = defvar
        self.children = (defvar,)



class Else_choice2(Node):
    def __init__(self, stmt, lineno):
        self.lineno = lineno
        self.stmt = stmt
        self.children = (stmt,)



class Expr1(Node):
    def __init__(self, expr, expr2, lineno):
        self.lineno = lineno
        self.expr = expr
        self.expr2 = expr2
        self.children = (expr, expr2,)



class Expr2(Node):
    def __init__(self, iden, clist, lineno):
        self.lineno = lineno
        self.iden = iden
        self.clist = clist
        self.children = (iden, clist,)



class Expr3(Node):
    def __init__(self, expr, expr2, expr3, lineno):
        self.lineno = lineno
        self.expr = expr
        self.expr2 = expr2
        self.expr3 = expr3
        self.children = (expr, expr2, expr3,)


class Expr4(Node):
    def __init__(self, expr, oper, expr2, lineno):
        self.lineno = lineno
        self.expr = expr
        self.oper = oper
        self.expr2 = expr2
        self.children = (expr, oper, expr2,)



class Expr5(Node):
    def __init__(self, oper, expr, lineno):
        self.lineno = lineno
        self.oper = oper
        self.expr = expr
        self.children = (oper, expr,)



class Expr6(Node):
    def __init__(self, clist, lineno):
        self.lineno = lineno
        self.clist = clist
        self.children = (clist,)


class Expr7(Node):
    def __init__(self, iden, lineno):
        self.lineno = lineno
        self.iden = iden
        self.children = (iden,)


#class Expr8(Node):
#    def __init__(self, iden, oper, expr, lineno):
#        self.lineno = lineno
#        self.iden = iden
#        self.oper = oper
#        self.expr = expr
#        self.children = (iden, expr,)


class Expr9(Node):
    def __init__(self, num, lineno):
        self.lineno = lineno
        self.num = num
        self.children = (num,)


class Type(Node):
    def __init__(self, type_value, lineno):
        self.lineno = lineno
        self.type_value = type_value
        self.children = (type_value,)

class Clist2(Node):
    def __init__(self, expr, lineno):
        self.lineno = lineno
        self.expr = expr
        self.children = (expr,)

class Clist3(Node):
    def __init__(self, expr, clist, lineno):
        self.lineno = lineno
        self.expr = expr
        self.clist = clist
        self.children = (expr, clist,)


class Defvar(Node):
    def __init__(self, type, iden, lineno):
        self.lineno = lineno
        self.type = type
        self.iden = iden
        self.children = (type, iden,)


class Defvar2(Node):
    def __init__(self, type, iden, expr, lineno):
        self.lineno = lineno
        self.type = type
        self.iden = iden
        self.expr = expr
        self.children = (type, iden, expr,)

class Flist2(Node):
    def __init__(self, type, iden, lineno):
        self.lineno = lineno
        self.type = type
        self.iden = iden
        self.children = (type, iden,)


class Flist3(Node):
    def __init__(self, type, iden, flist, lineno):
        self.lineno = lineno
        self.type = type
        self.iden = iden
        self.flist = flist
        self.children = (type, iden, flist,)



class Num(Node):
    def __init__(self, num_value, lineno):
        self.lineno = lineno
        self.num_value = num_value
        self.children = (num_value,)


class Iden(Node):
    def __init__(self, iden_value, lineno):
        self.lineno = lineno
        self.iden_value = iden_value
        self.children = (iden_value,)


class Empty(Node):
    def __init__(self, lineno):
        self.lineno = lineno
        self.name = ""
        self.children = ()
