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

