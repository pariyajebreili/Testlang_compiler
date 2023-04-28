from Lexical_Analyzer_PLY_package.tokenizer import tokenizer
from utils.syntax_tree import SyntaxTreeUtil
from utils.ast import *
import config


class Grammar(object):

    tokens = tokenizer.tokens

    def __init__(self, parser_messages):
        self.parser_messages = parser_messages



