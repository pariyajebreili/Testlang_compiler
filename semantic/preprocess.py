from utils.symbol_table import *
import utils.ast as AST
from utils.node_visitor import NodeVisitor
import config


class PreProcess(NodeVisitor):

    def __init__(self, semantic_messages):
        print(f"semantic init")
        self.create_and_push_builtin_funcs(config.global_symbol_table)
        self.semantic_messages = semantic_messages
    
    def visit_Prog1(self, node, table):
        print(f"visiting22: prog1")
        self.visit(node.func, config.global_symbol_table)

    def visit_Prog2(self, node, table):
        print(f"visiting22: prog2")
        self.visit(node.func, config.global_symbol_table)
        self.visit(node.prog, config.global_symbol_table)


    def visit_Func(self, node, table):
        print(f"visiting22: func")

        parameters = self.get_parameters(node)
        function_name= node.iden.iden_value["name"]


        name = node.iden.iden_value["name"]

        function_symbol = FunctionSymbol(name, node.type.type_value["name"], parameters)
        if not table.put(function_symbol):
            self.semantic_messages.add_message({"message":f"Identifier '{name}' Already Exists", "lineno":node.flist.lineno})
            return
        function_body_table = SymbolTable(table, function_name+"_function_body_block_table")
        for par in parameters:
            name = par["iden"].iden_value["name"]
            type = par["type"].type_value["name"]
            if not function_body_table.put(VariableSymbol(name, type)):
                self.semantic_messages.add_message({"message": f"'{name}' Already Defined", "lineno": node.flist.lineno})
        self.visit(node.body, function_body_table)
        

    def visit_Body1(self, node, table):
        print(f"visiting22: body1")
        self.visit(node.stmt, table)
            
    def visit_Body2(self, node, table):
        print(f"visiting22: body2")
        self.visit(node.stmt, table)
        self.visit(node.body, table)

    def visit_Stmt1(self, node, table):
        print(f"visiting22: stmt1")
        pass            

    def visit_Stmt2(self, node, table):
        print(f"visiting22: stmt2")
        self.visit(node.defvar, table)

    def visit_Stmt3(self, node, table):
        print(f"visiting22: stmt3")
        if_block_symbol_table = SymbolTable(table, f"if_block_{node.lineno}")
        self.visit(node.stmt, if_block_symbol_table)
        self.visit(node.else_choice, table)


    def visit_Else_choice1(self, node, table):
        print(f"visiting22: stmt4")
        pass


    def visit_Else_choice2(self, node, table):
        print(f"visiting22: stmt4")
        else_block_symbol_table = SymbolTable(table, f"else_block_{node.lineno}") 
        self.visit(node.stmt, else_block_symbol_table)


    def visit_Stmt5(self, node, table):
        print(f"visiting22: stmt5")
        for_block_symbol_table = SymbolTable(table, f"for_block_{node.lineno}") 
        
        name1 = node.iden1.iden_value["name"]
        type1 = "int"
        iden1 = VariableSymbol(name1, type1)
        for_block_symbol_table.put(iden1)
        
        self.visit(node.stmt, for_block_symbol_table)


    def visit_Stmt6(self, node, table):
        print(f"visiting22: stmt6")
        pass


    def visit_Stmt7(self, node, table):
        print(f"visiting22: stmt7")
        body_block_symbol_table = SymbolTable(table, f"body_block_{node.lineno}") 
        self.visit(node.body, body_block_symbol_table)

    
    def visit_Defvar(self, node, table):
        print(f"visiting22: defvar")
        pass

            
    def visit_Type(self, node, table):
        print(f"visiting22: type")
        pass

    def visit_Iden(self, node, table):
        print(f"visiting22: iden")
        pass

    def visit_Empty(self, node, table):
        print(f"visiting22: empty")
        pass



    def create_and_push_builtin_funcs(self, table):
        input_function_symbol = FunctionSymbol("input", "int", [] )
        table.put(input_function_symbol)

        print_funcition_symbol = FunctionSymbol("print", "int", [{"iden": "n", "type": "int"}] )
        table.put(print_funcition_symbol)

        vector_funcition_symbol = FunctionSymbol("list", "vector", [{"iden": "x", "type": "int"}] )
        table.put(vector_funcition_symbol)

        getVector_funcition_symbol = FunctionSymbol("getVector", "vector", [{"iden": "A", "type": "vector"}] )
        table.put(getVector_funcition_symbol)

        printVector_funcition_symbol = FunctionSymbol("printVector", "vector", [{"iden": "A", "type": "vector"}] )
        table.put(printVector_funcition_symbol)

        len_funcition_symbol = FunctionSymbol("len", "int", [{"iden": "A", "type": "vector"}] )
        table.put(len_funcition_symbol)

        exit_funcition_symbol = FunctionSymbol("exit", "int", [{"iden": "n", "type": "int"}] )
        table.put(exit_funcition_symbol)




    def get_parameters(self, node):
        parameters = []
        flist = node.flist
        if not isinstance(flist, AST.Empty):
            if flist.iden:
                parameters.append({"iden": flist.iden, "type": flist.type})
            while hasattr(flist, "flist"):
                flist = flist.flist
                if (not isinstance(flist, AST.Empty)):
                    parameters.append({"iden": flist.iden, "type": flist.type})
        parameters.reverse()
        return parameters