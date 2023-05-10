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
            {"message": "No Appropriate Parameters Defined Saeid", "lineno": self.last_message_line, "is_warning": True})
        p[4] = p[4].value
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



    def p_empty(self, p):
        '''empty :'''
        pass