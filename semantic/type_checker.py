from utils.symbol_table import *
import utils.ast as AST
from utils.node_visitor import NodeVisitor
import config


class TypeChecker(NodeVisitor):

    def __init__(self, semantic_messages):
        self.semantic_messages = semantic_messages
    

    def visit_Prog1(self, node, table):
        #print(f"visiting: prog1")
        self.visit(node.func, config.global_symbol_table)

    
    def visit_Prog2(self, node, table):
        #print(f"visiting: prog2")
        self.visit(node.func,config.global_symbol_table)
        self.visit(node.prog, config.global_symbol_table)


    def visit_Func(self, node, table):
        #print(f"visiting: func")
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



    def visit_Stmt4(self, node, table):
        #print(f"visiting: prog2")
        self.visit(node.func,config.global_symbol_table)

    

    def visit_Stmt5(self, node, table):
        #print(f"visiting: stmt5")
        expr_type = self.visit(node.expr, table)
        for_block_symbol_table = self.find_symbol_table(f"for_block_{node.lineno}", table)
        
        name1 = node.iden1.iden_value["name"]
        setattr(node, "type", expr_type)
        iden1 = VariableSymbol(name1, type)
        
        
        for_block_symbol_table.put(iden1)
        self.visit(node.stmt, for_block_symbol_table)




    def visit_Stmt6(self, node, table):
        #print(f"visiting: stmt6")
        res = self.visit(node.expr, table)
        function_name = []
        while not "_function_body_block_table" in table.name and table:
            table = table.parent
        if table:
            function_name = table.name.split("_function_body_block_table")[0]
            function_symbol = config.global_symbol_table.get(function_name)
            function_type = function_symbol.type
            if res != function_type:
                self.semantic_messages.add_message({"message": f"Returning Not Appropriate Value for Function '{function_name}'. Expected '{function_type}', Instead of '{res}'", "lineno":node.expr.lineno})
        else:
            self.semantic_messages.add_message({"message": f"NO Need to Return Value","lineno": node.expr.lineno})
            



    def visit_Stmt7(self, node, table):
        #print(f"visiting: stmt7")
        body_block_symbol_table = self.find_symbol_table(f"body_block_{node.lineno}", table)
        self.visit(node.body, body_block_symbol_table)


    def visit_Defvar(self, node, table):
        #print(f"visiting: defvar")
        name = node.iden.iden_value["name"]
        type = node.type.type_value["name"]
        if not table.put(VariableSymbol(name, type)):
                self.semantic_messages.add_message({"message": f"'{name}' Already Defined", "lineno":node.iden.lineno})
        self.visit(node.iden, table)
        self.visit(node.type, table)
    


    def visit_Expr1(self, node, table):
        # calling an array
        #print(f"visiting: expr2")
        type_of_array_iden = self.visit(node.expr, table)
        type_of_array_index = self.visit(node.expr2, table)
        if type_of_array_iden == "vector" and type_of_array_index == "int":
            return "int"

        else:
            self.semantic_messages.add_message({"message": f" Expected an Vector ", "lineno": node.expr.lineno})
            if type_of_array_index != "int":
                self.semantic_messages.add_message({"message": f'{node.expr.lineno}: Expected Numeric Value', "lineno": node.expr.lineno})
            return "none"


    def visit_Expr2(self, node, table):
        #function call
        #print(f"visiting: expr1")
        function_iden = node.iden.iden_value["name"]
        function_symbol = table.get(function_iden)
        if isinstance(function_symbol, FunctionSymbol):
            parameters = self.get_parameters(function_symbol)
            arguments = self.get_arguments(node, table)

            if len(parameters) != len(arguments):
                    self.semantic_messages.add_message({"message": f"Function '{function_iden}' Expected {len(parameters)} Arguments Not {len(arguments)}", "lineno": node.clist.lineno})
                    return function_symbol.type

            # check arguments types with parameters types
            for i in range(len(function_symbol.parameters)):
                par_type = parameters[i]
                arg_type = arguments[i]
                if par_type != arg_type:
                    self.semantic_messages.add_message({"message": f"{node.clist.lineno}: {i+1}th Argument of Function '{function_iden}' Expected '{par_type}'", "lineno":node.clist.lineno})
                    return function_symbol.type
            return function_symbol.type
        

        #function is not declared but it can be called becasue of error handling, it returns "none"        
        else:
            result = table.get(function_iden, check_parent=False)
            #if there is not a var with the same name in the same scope then it would make a function that returns "none" in the same scope
            if not result:
                self.semantic_messages.add_message({"message": f"Function: '{function_iden}' Not Defined", "lineno": node.iden.lineno})
                new_declared_func_for_error_handling = FunctionSymbol(function_iden, "none",[])
                table.put(new_declared_func_for_error_handling)

            #if there is a var in the same scope with this name, return it's type
            else:
                self.semantic_messages.add_message({"message": f"'{function_iden}' Is Not Declared AS a Function", "lineno": node.iden.lineno})
                return result.type



    def visit_Expr3(self, node, table):
        #print(f"visiting: expr3")
        condition_expr = self.visit(node.expr, table)
        true_block_expr = self.visit(node.expr2, table)
        false_block_expr = self.visit(node.expr3, table)
        if condition_expr == "none":
            return false_block_expr
        return true_block_expr



    def visit_Expr4(self, node, table):
        #print(f"visiting: expr4")
        first_operand = self.visit(node.expr, table)
        second_operand = self.visit(node.expr2, table)
        operator = node.oper["name"]

        #check if it's like id = expr
        first_operand_is_iden = isinstance(node.expr, AST.Expr7)
        if operator == "=" and first_operand == "none" and second_operand !="none" and first_operand_is_iden:
            first_operand_name = node.expr.iden.iden_value["name"]
            first_operand_symbol = table.get(first_operand_name)
            first_operand_symbol.type = second_operand
            first_operand = second_operand
            return second_operand

        if first_operand != second_operand:
            self.semantic_messages.add_message({"message": f" Not Equal In Type. '{first_operand}' Opposed To '{second_operand}'", "lineno":node.expr.lineno})
            return "none"
        return first_operand


    def visit_Expr5(self, node, table):
        #print(f"visiting: expr5")
        #operator
        operand = self.visit(node.expr, table)
        operator = node.oper["name"]
        if operand == "int" :
            return operand
        elif operand == "none" and operator == "not":
            return "int"
        elif operator == "not":
            self.semantic_messages.add_message({"message": f" Expected Operand Of '{operator}' Be Numeric or None", "lineno":node.expr.lineno})
            return "none"
        else:
            self.semantic_messages.add_message({"message": f" Expected Operand Of '{operator}' Be Numeric", "lineno":node.expr.lineno})
            return "none"



    def visit_Expr6(self, node, table):
        #print(f"visiting: expr6")
        return self.visit(node.expr, table)



    def visit_Expr7(self, node, table):
        #print(f"visiting: expr7")
        result = self.visit(node.iden, table)
        if not result:
            new_declared_symbol_for_error_handling = VariableSymbol(node.iden.iden_value["name"],"none")
            table.put(new_declared_symbol_for_error_handling)
            return "none"
        return result
        


    #def visit_Expr8(self, node, table):
    #    print(f"visiting: expr8")
    #    function_iden = node.iden.iden_value["name"]
        
    


    def visit_Expr9(self, node, table):
        #print(f"visiting: expr9")
        return self.visit(node.num, table)




    def visit_Clist1(self, node, table):
        #print(f"visiting: clist1")
        pass

    def visit_Clist2(self, node, table):
        #print(f"visiting: clist2")
        return self.visit(node.expr, table)
        
    def visit_Clist3(self, node, table):
        #print(f"visiting: clist3")
        self.visit(node.clist, table)
        return self.visit(node.expr, table)



    def visit_Type(self, node, table):
        #print(f"visiting: type")
        type = node.type_value["name"]
        return type

    def visit_Num(self, node, table):
        #print(f"visiting: num")
        return "int" 

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