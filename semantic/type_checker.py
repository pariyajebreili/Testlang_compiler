from utils.symbol_table import *
import utils.ast as AST
from utils.node_visitor import NodeVisitor
import config


class TypeChecker(NodeVisitor):

    def __init__(self, semantic_messages):
        self.semantic_messages = semantic_messages
    

    def visit_Prog1(self, node, table):
       pass
    
    
    def visit_Prog2(self, node, table):
        #print(f"visiting: prog2")
        self.visit(node.func,config.global_symbol_table)
        self.visit(node.prog, config.global_symbol_table)


    def visit_Func(self, node, table):
    #    #print(f"visiting: func")
        function_symbol = table.get(node.iden.iden_value["name"])
        function_name = function_symbol.name
        function_body_block = self.find_symbol_table(f"{function_name}_function_body_block_table", table)

        self.visit(node.body, function_body_block)

        

    def visit_Body1(self, node, table):
        #print(f"visiting: body1")
        self.visit(node.stmt, table)


    def visit_Body2(self, node, table):
        #print(f"visiting: body2")
        self.visit(node.stmt, table)
        self.visit(node.body, table)



    def visit_Stmt1(self, node, table):
        #print(f"visiting: stmt1")
        self.visit(node.expr, table)



    def visit_Stmt2(self, node, table):
        #print(f"visiting: stmt2")
        self.visit(node.defvar, table)



    def visit_Stmt3(self, node, table):
        #print(f"visiting: stmt3")
        self.visit(node.expr, table)
        if_block_symbol_table = self.find_symbol_table(f"if_block_{node.lineno}", table) 
        self.visit(node.stmt, if_block_symbol_table)
        self.visit(node.else_choice, table)



    def visit_Else_choice1(self, node, table):
        #print(f"visiting: stmt4")
        pass


    def visit_Else_choice2(self, node, table):
        #print(f"visiting: stmt4")
        else_block_symbol_table = self.find_symbol_table(f"else_block_{node.lineno}", table) 
        self.visit(node.stmt, else_block_symbol_table)



    def visit_Defvar1(self, node, table):
        #print(f"visiting: defvar")
        type = node.type.type_value["name"]
        name = node.iden.iden_value["name"]
        
        if not table.put(VariableSymbol(type, name)):
                self.semantic_messages.add_message({"message": f"'{name}' Already Defined", "lineno":node.iden.lineno})
        
        self.visit(node.type, table)
        self.visit(node.iden, table)
        

    #def visit_Defvar2(self, node, table):
    #    #print(f"visiting: defvar")
    #    name = node.iden.iden_value["name"]
    #    type = node.type.type_value["name"]
        

    #    if not table.put(VariableSymbol(type, name)):
    #            self.semantic_messages.add_message({"message": f"'{name}' Already Defined", "lineno":node.iden.lineno})
        
    #    self.visit(node.type, table)
    #    self.visit(node.iden, table)
    #    self.visit(node.expr, table)

    def visit_Expr1(self, node, table):
        # calling an array
        #print(f"visiting: expr2")
        type_of_vector = self.visit(node.expr, table)
        type_of_int = self.visit(node.expr2, table)
        if type_of_vector == "vector" and type_of_int == "num":
            return "num"

        else:
            self.semantic_messages.add_message({"message": f" Expected an vector ", "lineno": node.expr.lineno})
            if type_of_vector != "num":
                self.semantic_messages.add_message({"message": f'{node.expr.lineno}: Expected Numeric Value', "lineno": node.expr.lineno})
            return "none"












    def visit_Type(self, node, table):
        #print(f"visiting: type")
        type = node.type_value["name"]
        return type

    def visit_Num(self, node, table):
        #print(f"visiting: num")
        return "num" 

    def visit_Iden(self, node, table):
        #print(f"visiting: iden")
        name = node.iden_value["name"]
        symbol = table.get(name)
        if not symbol:
            self.semantic_messages.add_message({"message": f"'{name}' Is Not Declared", "lineno":node.lineno,  'is_warning': True})
            new_declared_variable_for_error_handling = FunctionSymbol(name, "none", [])
            table.put(new_declared_variable_for_error_handling)
            return "none"
        return symbol.type

    def visit_Empty(self, node, table):
        #print(f"visiting: empty")
        pass

    def find_symbol_table(self, name, parent):
        for i in range(len(parent.children)):
            if parent.children[i].name == name:
                return parent.children[i]

    def get_parameters(self, function_symbol):
        parameters = []
        for parameter in function_symbol.parameters:
            try:
                parameter = parameter["type"].type_value["name"]
            except:
                parameter =  parameter["type"]
            parameters.append(parameter)
        parameters.reverse()
        return parameters


    def get_arguments(self, node, table):
        arguments = []
        clist = node.clist
        if not isinstance(clist, AST.Empty):
            if clist.expr:
                res = self.visit(clist, table)
                if not isinstance(res, str) and res:
                    res = res.type_value["name"]
                arguments.append(res)
                while hasattr(clist, "clist"):
                    clist = clist.clist
                    if (not isinstance(clist, AST.Empty)):
                        res = self.visit(clist, table)
                        if not isinstance(res, str):
                            res = res.type_value["name"]
                        arguments.append(res)
        return arguments