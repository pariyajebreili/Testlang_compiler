from Lexical_Analyzer_PLY_package.tokens_file import Tokens   
from utils.syntax_tree import SyntaxTreeUtil
from utils.ast import *
import config


class Grammar(object):

    tokens = Tokens.tokens

    def __init__(self, parser_messages):
        self.parser_messages = parser_messages



    def p_prog1(self, p):
        '''prog : empty'''
        p[0] = "prog"
        p[0] = {
            "name": "prog",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),  
            "ast": Empty(self.lexer.lineno)
        }
        #config.syntax_tree = p[0]["st"]
        #config.ast = p[0]["ast"]



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
            {"message": "No Appropriate Parameters Defined Saeid", "lineno": self.last_message_line, "is_warning": True})
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







    def p_defvar1(self, p):
        '''defvar : VAR type iden'''
        #
        p[0] = "defvar"
        p[0] = {
            "name": "defvar",
            "lineno": self.lexer.lineno,
            "st": SyntaxTreeUtil.create_node(p),
            "ast": Defvar1(p[2]["ast"], p[3]["ast"], self.lexer.lineno)
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