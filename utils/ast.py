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
    def __init__(self, lineno):
        self.lineno = lineno
        #self.func = func
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



class Else_choice2(Node):
    def __init__(self, stmt, lineno):
        self.lineno = lineno
        self.stmt = stmt
        self.children = (stmt,)





class Type(Node):
    def __init__(self, type_value, lineno):
        self.lineno = lineno
        self.type_value = type_value
        self.children = (type_value,)


class Defvar1(Node):
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
