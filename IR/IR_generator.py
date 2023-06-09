from my_utils.symbol_table import *
import my_utils.ast as AST
from my_utils.node_visitor import NodeVisitor
import config


class IRGenerator(NodeVisitor):

    def __init__(self):
        self.reginster_index = 0
        self.label_index = 0
        self.memory_allocated_registers = []
        self.create_and_push_builtin_funcs()
        config.max_register_index_used_in_code = 0
    
    
    def visit_Prog1(self, node, table):
        print(f"visiting: prog1")
        func_code = self.visit(node.func, config.global_symbol_table)
        code = func_code

        self.builtin_funcs.reverse()
        for i in range(len(self.builtin_funcs)):
            if self.builtin_funcs[i]["used"] and not self.builtin_funcs[i]["included"] :
                code = f'''{self.builtin_funcs[i]["code"]}
{code}'''
                self.builtin_funcs[i]["included"] = True
        config.iR_code = code
        return code

    def visit_Prog2(self, node, table):
        print(f"visiting: prog2")
        func_code = self.visit(node.func,config.global_symbol_table)
        prog_code = self.visit(node.prog, config.global_symbol_table)
        func_name = node.func.iden.iden_value["name"]

        if func_name == "main":
            code = prog_code  + "\n" + func_code
        else:
            code = func_code + "\n" + prog_code

        self.builtin_funcs.reverse()
        for i in range(len(self.builtin_funcs)):
            if self.builtin_funcs[i]["used"] and not self.builtin_funcs[i]["included"] :
                code = f'''{self.builtin_funcs[i]["code"]}
{code}'''
                self.builtin_funcs[i]["included"] = True

        config.iR_code = code
        return code



    def visit_Func(self, node, table):
        print(f"visiting: func")
        function_iden= node.iden.iden_value["name"]
        function_symbol = table.get(function_iden)
        function_iden = function_symbol.name
        function_body_block = self.find_symbol_table(f"{function_iden}_function_body_block_table", table)

        parameters = self.get_parameters(node)

        self.reginster_index = 0
        parameters_initiation_code = ""
        for param in parameters:
            self.initiate_var_symbol_register(param["iden"].iden_value["name"], function_body_block)


        func_body_code = self.visit(node.body, function_body_block)
        code = f'''proc {function_iden}
{parameters_initiation_code}
{func_body_code}'''
        return code
        

    def visit_Body1(self, node, table):
        print(f"visiting: body1")
        stmt_code = self.visit(node.stmt, table)
        code = stmt_code
        if not stmt_code:
            code = ""
        else:
            code = stmt_code
        return code


    def visit_Body2(self, node, table):
        print(f"visiting: body2")
        stmt_code = self.visit(node.stmt, table)
        body_code = self.visit(node.body, table)

        if not stmt_code:
            code = body_code
        else:
            code = f'''{stmt_code}{body_code}'''
        return code 

    def visit_Stmt1(self, node, table):
        print(f"visiting: stmt1")
        res = self.visit(node.expr, table)
        if res:
            expr_code = res["code"]
            code = expr_code
        else: 
            code =""
        return code


    def visit_Stmt6(self, node, table):
        print(f"visiting: stmt6")
        res = self.visit(node.expr, table)
        expr_code = res["code"]
        expr_returned_reg = res["reg"]

        if table.name == "main_function_body_block_table":
            code = f'''{expr_code}
\tmov r0, {expr_returned_reg}
{self.get_release_memory_codes()}
\tret'''
        else:
            code = f'''{expr_code}
\tmov r0, {expr_returned_reg}
\tret'''
        return code
            


            
    def visit_Expr1(self, node, table):
        print(f"visiting: expr1")
        function_iden = node.iden.iden_value["name"]
        for i in range(len(self.builtin_funcs)):
            if function_iden == self.builtin_funcs[i]["name"] :
                self.builtin_funcs[i]["used"] = True

        arguments = self.get_arguments(node, table)

        arguments_registers_string = ""
        arguments_codes_string = ""

        returning_reg = self.create_register()

        if function_iden == "Array":
            self.memory_allocated_registers.append(returning_reg)
        
        for i in range(len(arguments)):
            if i == 0:
                if len(arguments) == 1:
                    arguments_registers_string += f"{returning_reg}"
                else:
                     arguments_registers_string += f"{returning_reg}, "
                arguments_codes_string += f'''{arguments[i]['code']}
\tmov {returning_reg}, {arguments[0]["reg"]}'''


            elif i == len(arguments) - 1: 
                arguments_registers_string += f"{arguments[i]['reg']}"
                arguments_codes_string += f"{arguments[i]['code']}"

            else:
                arguments_registers_string += f"{arguments[i]['reg']}, "
                arguments_codes_string += f"{arguments[i]['code']}, "


        if not arguments:
            return {"reg": returning_reg, 
            "code" : f'''\tcall {function_iden}, {returning_reg}'''}


        else:            
            return {"reg": returning_reg, 
            "code" : f'''{arguments_codes_string}
\tcall {function_iden}, {arguments_registers_string}'''}



    def visit_Expr2(self, node, table):
        print(f"visiting: expr2")
        res = self.visit(node.expr, table)
        array_iden_reg = res["reg"]

        res2 = self.visit(node.expr2, table)
        expr2_returned_code = res2["code"]
        expr2_returned_reg = res2["reg"]

        tmp_reg = self.create_register()
        tmp_reg2 = self.create_register()
        tmp_reg3 = self.create_register()
        tmp_reg4 = self.create_register()


       
        return {"reg": tmp_reg4, "addr":tmp_reg3,
        "code" : f'''{expr2_returned_code}
\tmov {tmp_reg}, 1
\tmov {tmp_reg2}, 8
\tadd {tmp_reg}, {expr2_returned_reg}, {tmp_reg}
\tmul {tmp_reg2}, {tmp_reg}, {tmp_reg2}
\tadd {tmp_reg3}, {array_iden_reg}, {tmp_reg2}
\tld {tmp_reg4}, {tmp_reg3}'''}




    def visit_Expr3(self, node, table):
        print(f"visiting: expr3")
        res = self.visit(node.expr, table)
        expr_returned_code = res["code"]
        expr_returned_reg = res["reg"]

        res2 = self.visit(node.expr2, table)
        expr2_returned_code = res2["code"]
        expr2_returned_reg = res2["reg"]

        res3 = self.visit(node.expr3, table)
        expr3_returned_code = res3["code"]
        expr3_returned_reg = res3["reg"]

        
        tmp_reg = self.create_register()
        label = self.create_label()
        label2 = self.create_label()
        return {"reg": tmp_reg, 
        "code" : f'''{expr_returned_code}
\tjz {expr_returned_reg}, {label}
{expr2_returned_code}
\tmov {tmp_reg}, {expr2_returned_reg}
\jmp {label2}
{label}:
{expr3_returned_code}
\tmov {tmp_reg}, {expr3_returned_reg}
{label2}:'''}




    def visit_Expr4(self, node, table):
        print(f"visiting: expr4")
        operator = node.oper["name"]

        res = self.visit(node.expr, table)
        expr_returned_code = res["code"]
        expr_returned_reg = res["reg"]

        res2 = self.visit(node.expr2, table)
        expr2_returned_code = res2["code"]
        expr2_returned_reg = res2["reg"]

        if operator == "=":
            if isinstance(node.expr, AST.Expr2):
                address_of_that_cell_of_array = res["addr"]
                tmp_reg = self.create_register()
                return {"reg": tmp_reg, 
                "code" : f'''
{expr_returned_code}
{expr2_returned_code}
\tst {expr2_returned_reg}, {address_of_that_cell_of_array}'''}   

            else:
                return {"reg": expr_returned_reg, 
                "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tmov {expr_returned_reg}, {expr2_returned_reg}'''}
        
        if operator == "+":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tadd {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}
        
        if operator == "-":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tsub {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == "*":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tmul {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}
        
        if operator == "/":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tdiv {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == "%":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tmod {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}
        
        if operator == "<":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp< {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == ">":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp> {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == "==":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp= {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}
        
        if operator == "<=":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp<= {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == ">=":
            tmp_reg = self.create_register()
            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp>= {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}'''}

        if operator == "!=":
            tmp_reg = self.create_register()
            label = self.create_label()
            label2 = self.create_label()

            return {"reg": tmp_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tcmp= {tmp_reg}, {expr_returned_reg}, {expr2_returned_reg}
\tjz {tmp_reg}, {label}
\tmov {tmp_reg}, 0
\tjmp {label2}
{label}:
\tmov {tmp_reg}, 1
{label2}:'''}

        if operator == "or":
            label = self.create_label()
            label2 = self.create_label()
            label3 = self.create_label()
            
            return {"reg": expr_returned_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tjz {expr_returned_reg}, {label}
\tmov {expr_returned_reg}, 1
\tjmp {label3}
{label}: 
\tjz {expr2_returned_reg}, {label2}
\tmov {expr_returned_reg}, 1
\tjmp {label3}
{label2}: 
\tmov {expr_returned_reg}, 0
{label3}:'''}

        if operator == "and":
            label = self.create_label()
            label2 = self.create_label()
            label3 = self.create_label()
            
            return {"reg": expr_returned_reg, 
            "code" : f'''{expr_returned_code}
{expr2_returned_code}
\tjz {expr_returned_reg}, {label2}
\tjz {expr2_returned_reg}, {label2}
{label}:
\tmov {expr_returned_reg}, 1
\tjmp {label3}
{label2}:
\tmov {expr_returned_reg}, 0
{label3}:'''}


    def visit_Expr5(self, node, table):
        #print(f"visiting: expr5")
        operator = node.oper["name"]

        res = self.visit(node.expr, table)
        expr_returned_code = res["code"]
        expr_returned_reg = res["reg"]


        if operator == "not":
            label = self.create_label()
            label2 = self.create_label()
            return {"reg": expr_returned_reg, 
            "code" : f'''{expr_returned_code}
\tjz {expr_returned_reg}, {label}
\tmov {expr_returned_reg}, 0
\tjmp {label2}
{label}:
\tmov {expr_returned_reg}, 1
{label2}:'''}

        if operator == "+":
            return {"reg": expr_returned_reg,
            "code" : expr_returned_code}
        
        if operator == "-":
            tmp_reg = self.create_register()
            return {"reg": expr_returned_reg,
            "code" : f'''{expr_returned_code}
\tmov {tmp_reg}, 2
\tmul {tmp_reg}, {expr_returned_reg}, {tmp_reg}
\tsub {expr_returned_reg}, {tmp_reg}, {expr_returned_reg}'''}



    def visit_Expr6(self, node, table):
        #print(f"visiting: expr6")
        res = self.visit(node.expr, table)
        expr_returned_code = res["code"]
        expr_returned_reg = res["reg"]
        return {"reg": expr_returned_reg,
        "code" : expr_returned_code}


    def visit_Expr7(self, node, table):
        print(f"visiting: expr7")
        name = node.iden.iden_value["name"]

        iden_reg = ""
        if hasattr(table.get(name), "reg"):
            iden_reg = table.get(name).reg
  
        else:
            reg = self.initiate_var_symbol_register(name, table)
            iden_reg = reg
        return {"reg": iden_reg,
        "code" : ""}
        

    def visit_Expr9(self, node, table):
        print(f"visiting: expr9")
        num = self.visit(node.num, table)
        num_reg = self.create_register()
        return {"reg": num_reg ,
        "code" : f'''
\tmov {num_reg}, {num}'''}


    def visit_Clist1(self, node, table):
        print(f"visiting: clist1")
        pass


    def visit_Clist2(self, node, table):
        print(f"visiting: clist2")
        return self.visit(node.expr, table)
        

    def visit_Clist3(self, node, table):
        print(f"visiting: clist3")
        self.visit(node.clist, table)
        return self.visit(node.expr, table)
    

    def visit_Num(self, node, table):
        print(f"visiting: num")
        num = node.num_value["name"]
        return num



    builtin_funcs = []
    def create_and_push_builtin_funcs(self):

        self.builtin_funcs.append({"name":"scan", "used":False, "included":False,
        "code":'''proc scan
\tcall iget, r0
\tret'''})


        self.builtin_funcs.append({"name":"print", "used":False, "included":False,
        "code":'''proc print
\tcall iput, r0
\tret'''})



    
        self.builtin_funcs.append({"name":"vector", "used":False, "included":False,
        "code":'''proc vector
\tmov r1, 1
\tadd r1, r0, r1
\tmov r2, 8
\tmul r2, r1, r2
\tcall mem, r2
\tst r0, r2
\tmov r0, r2
\tret'''})


        self.builtin_funcs.append({"name":"getVector", "used":False, "included":False,
        "code":'''proc getVector
\tld r1, r0
\tmov r2, 1   
\tmov r3, 8   
label_getArray:
\tcmp<= r4, r2, r1
\tjz r4, label2_getArray
\tmul r4, r2, r3
\tadd r5, r0, r4
\tcall iget, r6
\tst r6, r5
\tmov r7, 1
\tadd r2, r2, r7
\tjmp label_getArray
label2_getArray:
\tret'''})


        self.builtin_funcs.append({"name":"printArray", "used":False, "included":False,
        "code":'''proc printArray
\tld r1, r0
\tmov r2, 1   
\tmov r3, 8   
label_printArray:
\tcmp<= r4, r2, r1
\tjz r4, label2_printArray
\tmul r4, r2, r3
\tadd r5, r0, r4
\tld r6, r5
\tcall iput, r6
\tmov r7, 1
\tadd r2, r2, r7
\tjmp label_printArray
label2_printArray:
\tret'''})


        self.builtin_funcs.append({"name":"len", "used":False, "included":False,
        "code":'''proc len
\tld r1, r0
\tmov r0, r1
\tret'''})



    def create_register(self):
        if self.reginster_index > config.max_register_index_used_in_code:
            config.max_register_index_used_in_code = self.reginster_index
        self.reginster_index += 1
        return f"r{self.reginster_index - 1}"

    
    def create_label(self, name=None):
        self.label_index += 1
        if name:
            return f"{name}{self.label_index - 1}"
        return f"label{self.label_index - 1}"


    def find_symbol_table(self, name, parent):
        for i in range(len(parent.children)):
            if parent.children[i].name == name:
                return parent.children[i]


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
        return parameters


    def get_arguments(self, node, table):
        arguments = []
        clist = node.clist
        if not isinstance(clist, AST.Empty):
            if clist.expr:
                res = self.visit(clist, table)
                expr_returned_code = res["code"]
                expr_returned_reg = res["reg"]
                if not isinstance(res, str) and res:
                    res = expr_returned_reg
                arguments.append({"reg": expr_returned_reg, "code": expr_returned_code})
                while hasattr(clist, "clist"):
                    clist = clist.clist
                    if (not isinstance(clist, AST.Empty)):
                        res = self.visit(clist, table)
                        expr_returned_code = res["code"]
                        expr_returned_reg = res["reg"]
                        if not isinstance(res, str):
                            res = expr_returned_reg
                        arguments.append({"reg": expr_returned_reg, "code": expr_returned_code})
        return arguments

    def initiate_var_symbol_register(self, name, table):
        var_symbol = table.get(name)
        reg = self.create_register()
        setattr(var_symbol, "reg", reg)
        return reg

    
    def update_var_symbol_register(self, name, value, table):
        var_symbol = table.get(name)
        code = f"\tmov {var_symbol}, {value}"
        return code


    def get_release_memory_codes(self):
        code = ""
        for reg in self.memory_allocated_registers:
            code +=f"\n\tcall rel, {reg}"
        return code
