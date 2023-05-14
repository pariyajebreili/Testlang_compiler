from lexer.tokens import Tokens   
from utils.syntax_tree import SyntaxTreeUtil
from utils.ast import *
import config


class Grammar(object):

    tokens = Tokens.tokens

    def __init__(self, parser_messages):
        self.parser_messages = parser_messages



    def p_prog1(self, p):
        '''prog : func'''
        p[0] = "prog"
        p[0] = {
            "name": "prog",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),  
            "ast": Prog1(p[1]["ast"], self.lexer.lineno)
        }
        config.syntax_tree = p[0]["st"]
        config.ast = p[0]["ast"]



    def p_prog2(self, p):
        '''prog : func prog'''
        p[0] = "prog"
        p[0] = {
            "name": "prog",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),  
            "ast": Prog2(p[1]["ast"], p[2]["ast"], self.lexer.lineno)
        }
        config.syntax_tree = p[0]["st"]
        config.ast = p[0]["ast"]


    def p_func(self, p):
        '''func : DEF type iden LPAREN flist RPAREN LBRACE body RBRACE'''
        p[0] = "func"
        p[0] = {
            "name": "func",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Func(p[2]["ast"], p[3]["ast"], p[5]["ast"], p[8]["ast"], self.lexer.lineno)
        }




    def p_func_error(self, p):  
        '''func : DEF type iden LPAREN error RPAREN LBRACE body RBRACE'''
        self.parser_messages.add_message(
            {"message": "No Appropriate Parameters Defined", "lineno": self.last_message_line, "is_warning": True})
        p[5] = p[5].value
        p[0] = "func"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Func(p[2]["ast"], p[3]["ast"], p[5], p[8]["ast"], self.lexer.lineno)
        }

    def p_body1(self, p):
        '''body : stmt'''
        p[0] = "body"
        p[0] = {
            "name": "body",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Body1(p[1]["ast"], self.lexer.lineno)
        }

    def p_body2(self, p):
        '''body : stmt body'''
        p[0] = "body"
        p[0] = {
            "name": "body",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Body2(p[1]["ast"], p[2]["ast"], self.lexer.lineno)
        }



    def p_stmt1(self, p):
        '''stmt : expr SEMI_COLON'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt1(p[1]["ast"], self.lexer.lineno)
        }


    def p_stmt2(self, p):
        '''stmt : defvar SEMI_COLON'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt2(p[1]["ast"], self.lexer.lineno)
        }



    def p_stmt3(self, p):
        '''stmt : IF LPAREN expr RPAREN stmt else_choice'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt3(p[3]["ast"], p[5]["ast"], p[6]["ast"], self.lexer.lineno)
        }  


    def p_stmt3_error(self, p):  
        '''stmt : IF LPAREN error RPAREN stmt else_choice'''
        self.parser_messages.add_message(
            {"message": "Not Appropriate Value", "lineno": self.last_message_line, "is_warning": True})
        p[4] = p[3].value
        p[0] = "stmt"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt3(p[3], p[5]["ast"], p[6]["ast"], self.lexer.lineno)
        }


    def p_else_choice1(self, p):
        '''else_choice : empty'''
        p[0] = "else_choice"
        p[0] = {
            "name": "else_choice",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Empty(self.lexer.lineno)
        }

    def p_else_choice2(self, p):
        '''else_choice : ELSE stmt'''
        p[0] = "else_choice"
        p[0] = {
            "name": "else_choice",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Else_choice2(p[2]["ast"], self.lexer.lineno)
        }


    def p_stmt4(self, p):
        '''stmt : func'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt4(p[1]["ast"], self.lexer.lineno)
        }

        
    def p_stmt5(self, p):
        '''stmt : FOR LPAREN expr TO expr RPAREN stmt'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt5(p[3]["ast"], p[5]["ast"], p[7]["ast"], self.lexer.lineno)
        }

        
    def p_stmt6(self, p):
        '''stmt : RETURN expr SEMI_COLON'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt6(p[2]["ast"], self.lexer.lineno)
        }

    def p_stmt7(self, p):
        '''stmt : LBRACE body RBRACE'''
        p[0] = "stmt"
        p[0] = {
            "name": "stmt",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Stmt7(p[2]["ast"], self.lexer.lineno)
        }


    #def p_stmt8(self, p):
    #    '''stmt : WHILE LPAREN expr RPAREN stmt'''
    #    p[0] = "stmt"
    #    p[0] = {
    #        "name": "stmt",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Stmt8(p[3]["ast"], p[5]["ast"], self.lexer.lineno)
    #    }


    #def p_expr1(self, p):
    #    '''expr : expr LSQUAREBR expr RSQUAREBR'''
    #    p[0] = "expr"
    #    p[0] = {
    #        "name": "expr",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Expr1(p[1]["ast"], p[3]["ast"], self.lexer.lineno)
    #    }


    #def p_expr1_error(self, p):
    #    '''expr : expr LSQUAREBR error RSQUAREBR'''
    #    self.parser_messages.add_message(
    #        {"message": "No Appropraite Arguments", "lineno": self.last_message_line, "is_warning": True})
    #    p[3] = p[3].value
    #    p[0] = "expr"
    #    p[0] = {
    #        "name": "expr",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Expr1(p[1]["ast"], p[3], self.lexer.lineno)
    #    }



    #def p_expr2(self, p):
    #    '''expr : iden LPAREN clist RPAREN'''
    #    p[0] = "expr"
    #    p[0] = {
    #        "name": "expr",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Expr1(p[1]["ast"], p[3]["ast"], self.lexer.lineno)
    #    }

    #def p_expr2_error(self, p):
    #    '''expr : iden LPAREN error RPAREN'''
    #    self.parser_messages.add_message(
    #        {"message": "No Appropraite Arguments", "lineno": self.last_message_line, "is_warning": True})
    #    p[3] = p[3].value
    #    p[0] = "expr"
    #    p[0] = {
    #        "name": "expr",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Expr1(p[1]["ast"], p[3], self.lexer.lineno)
    #    }


    def p_expr1(self, p):
        '''expr : iden LPAREN clist RPAREN'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr1(p[1]["ast"], p[3]["ast"], self.lexer.lineno)
        }
    def p_expr1_error(self, p):
        '''expr : iden LPAREN error RPAREN'''
        self.parser_messages.add_message(
            {"message": "No Appropraite Arguments", "lineno": self.last_message_line, "is_warning": True})
        p[3] = p[3].value
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr1(p[1]["ast"], p[3], self.lexer.lineno)
        }

    def p_expr2(self, p):
        '''expr : expr LSQUAREBR expr RSQUAREBR'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr2(p[1]["ast"], p[3]["ast"], self.lexer.lineno)
        }

    def p_expr2_error(self, p):  
        '''expr : expr LSQUAREBR error RSQUAREBR'''
        self.parser_messages.add_message(
            {"message": "No Appropraite Value", "lineno": self.last_message_line, "is_warning": True})
        p[3] = p[3].value
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr1(p[1]["ast"], p[3], self.lexer.lineno)
        }


    def p_expr3(self, p):
        '''expr : expr QMARK expr COLON expr'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr3(p[1]["ast"], p[3]["ast"], p[5]["ast"], self.lexer.lineno)
        }

    def p_expr4(self, p):
        '''expr : expr PARITY expr 
                 | expr NOT_EQ expr 
                 | expr DIVIDE expr
                 | expr TIMES expr
                 | expr MINUS expr
                 | expr PLUS expr
                 | expr MOD expr 
                 | expr GREATER_EQUAL expr 
                 | expr LESS_EQUAL expr 
                 | expr GREATER_THAN expr
                 | expr LESS_THAN expr
                 | expr OR expr 
                 | expr AND expr 
                 | expr EQ expr'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr4(p[1]["ast"], p[2], p[3]["ast"], self.lexer.lineno)
        }

    def p_expr5(self, p):
        '''expr : MINUS expr 
                 | PLUS expr 
                 | NOT expr'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr5(p[1], p[2]["ast"], self.lexer.lineno)
        }

    def p_expr6(self, p):
        '''expr : LSQUAREBR clist RSQUAREBR'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr6(p[2]["ast"], self.lexer.lineno)
        }

    def p_expr6_error(self, p):
        '''expr : LSQUAREBR error RSQUAREBR'''
        self.parser_messages.add_message(
            {"message": "No Appropriate Value For List", "lineno": self.last_message_line, "is_warning": True})
        p[2] = p[2].value
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr6(p[2], self.lexer.lineno)
        }


    def p_expr7(self, p):
        '''expr : iden'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr7(p[1]["ast"], self.lexer.lineno)
        }



    #def p_expr8(self, p):
    #    '''expr : iden EQ expr'''
    #    p[0] = "expr"
    #    p[0] = {
    #        "name": "expr",
    #        "lineno": self.lexer.lineno,
    #        "st": SyntaxTreeUtil.create_node(p),
    #        "ast": Expr8(p[1]["ast"], p[2], p[3]["ast"], self.lexer.lineno)
    #    }



    def p_expr9(self, p):
        '''expr : num'''
        p[0] = "expr"
        p[0] = {
            "name": "expr",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Expr9(p[1]["ast"], self.lexer.lineno)
        }




    def p_clist1(self, p):
        '''clist : empty'''
        p[0] = "clist"
        p[0] = {
            "name": "clist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Empty(self.lexer.lineno)
        }

    def p_clist2(self, p):
        '''clist : expr'''
        p[0] = "clist"
        p[0] = {
            "name": "clist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Clist2(p[1]["ast"], self.lexer.lineno)
        }

    def p_clist3(self, p):
        '''clist : expr COMMA clist'''
        p[0] = "clist"
        p[0] = {
            "name": "clist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Clist3(p[1]["ast"], p[3]["ast"], self.lexer.lineno)
        }




    def p_defvar1(self, p):
        '''defvar : VAR type iden'''
        #
        p[0] = "defvar"
        p[0] = {
            "name": "defvar",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Defvar(p[2]["ast"], p[3]["ast"], self.lexer.lineno)
        }



    def p_defvar2(self, p):
        '''defvar : VAR type iden EQ expr'''
        #
        p[0] = "defvar"
        p[0] = {
            "name": "defvar",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Defvar2(p[2]["ast"], p[3]["ast"], p[5]["ast"], self.lexer.lineno)
        }


    def p_flist1(self, p):
        '''flist : empty'''
        p[0] = "flist"
        p[0] = {
            "name": "flist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Empty(self.lexer.lineno)
        }

    def p_flist2(self, p):
        '''flist : type iden'''
        p[0] = "flist"
        p[0] = {
            "name": "flist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Flist2(p[1]["ast"], p[2]["ast"], self.lexer.lineno)
        }

    def p_flist3(self, p):
        '''flist : type iden COMMA flist'''
        p[0] = "flist"
        p[0] = {
            "name": "flist",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Flist3(p[1]["ast"], p[2]["ast"], p[4]["ast"], self.lexer.lineno)
        }

        

    def p_iden(self, p):
        '''iden : IDEN'''
        p[0] = "iden"
        p[0] = {
            "name": "iden",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Iden(p[1], self.lexer.lineno)
        }
       


    def p_type(self, p):
        '''type : INT
                | VECTOR
                | NULL'''
        p[0] = "type"
        p[0] = {
            "name": "type",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Type(p[1], self.lexer.lineno)
        }

    

    def p_num(self, p):
        '''num : NUM'''
        p[0] = "number"
        p[0] = {
            "name": "number",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Num(p[1], self.lexer.lineno)
        }

    def p_empty(self, p):
        '''empty :'''
        pass


    def p_error(self, p):
        if p:
            self.parser_messages.add_message(
                {"message": f"Syntax Error at Token: {p.value}", "lineno": self.lexer.lineno})
            self.last_message_line = self.lexer.lineno
        else:
            self.parser_messages.add_message(
                {"message": "Syntax Error at EOF", "lineno": self.lexer.lineno})
    


    precedence = (
        ('left', 'error'),
        ('left', 'AND', 'OR'),
        ('left', 'NOT', 'LESS_EQUAL', 'GREATER_EQUAL','NOT_EQ', 'PARITY', 'LESS_THAN', 'GREATER_THAN'),
        ('left', 'EQ', 'QMARK', 'COLON'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD'),
        ('left', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE')
    )
