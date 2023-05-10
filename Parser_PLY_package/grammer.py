from Lexical_Analyzer_PLY_package.tokens_file import Tokens   
from utils.syntax_tree import SyntaxTreeUtil
from utils.ast import *
import config


class Grammar(object):

    tokens = Tokens.tokens

    def __init__(self, parser_messages):
        self.parser_messages = parser_messages


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