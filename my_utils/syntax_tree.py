from anytree import NodeMixin
import uuid


class SyntaxTreeNode(NodeMixin):  
    def __init__(self, name, id, children=None):
        self.name = name
        self.id = id
        if children:
            self.children = children

class SyntaxTreeUtil(object):
    
    @staticmethod
    def create_node(p):
        id = uuid.uuid4()
        children = []
        for i in range(len(list(p))):
            if i == 0:
                continue
            try:
                children.append(p[i]["st"])
            except:
                name = p[i]
                node = SyntaxTreeUtil.create_node([p[i]])
                p[i] = {
                    "name":name,
                    "st": node,
                }
                children.append(p[i]["st"])

        node = SyntaxTreeNode(p[0], id, children=children)
        return node
