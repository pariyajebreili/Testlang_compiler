class Symbol:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class VariableSymbol(Symbol):
    pass

class ArraySymbol(Symbol):
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

class FunctionSymbol(Symbol):
    def __init__(self, name, type, parameters):
        self.name = name
        self.type = type
        self.parameters = parameters

class SymbolTable(object):

    def __init__(self, parent, name):
        self.symbols = {}
        self.name = name
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    def put(self, symbol):
        if self.symbols.__contains__(symbol.name):
            return False
        else:
            self.symbols[symbol.name]= symbol
            return True

    def get(self, name, check_parent=True):
        if self.symbols.__contains__(name):
            return self.symbols[name]
        elif check_parent and self.parent:
            return self.parent.get(name)
        else:
            return None


    def getParentScope(self):
        return self.parent





