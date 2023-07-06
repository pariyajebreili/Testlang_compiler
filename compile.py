from my_utils.symbol_table import SymbolTable
from Lexical_Analyzer_PLY_package.tokens import Tokens
from Lexical_Analyzer_PLY_package.lexer import Lexer
from Parser_PLY_package.grammer import Grammar
from Parser_PLY_package.parser import Parser
from semantic.type_checker import TypeChecker
from semantic.preprocess import PreProcess
from my_utils.show_tree import show_tree
import config
from my_utils.colorprints import ColorPrints
import os 


class Compiler(object):
    def __init__(self):
        config.global_symbol_table = SymbolTable(None, "global")
        self.lexer_messages = CompilerMessages()
        self.parser_messages = CompilerMessages()
        self.semantic_messages = CompilerMessages()

        self.tokens = Tokens(self.lexer_messages)
        self.lexer = Lexer(self.tokens)

        self.grammar = Grammar(self.parser_messages)
        self.grammar.lexer = self.lexer.lexer
        self.parser = Parser(self.grammar)

        self.type_checker = TypeChecker(self.semantic_messages)
        self.preprocess = PreProcess(self.semantic_messages)
        self.compiled_failed = False



    def compile(self, data, show_syntax_tree=False, print_messages=True):

        self.lexer.build(data)
        if data.strip() == "":
            ColorPrints.print_in_red("No Code For Generting!")
            return
        self.parser.build(data)
        try:
            if show_syntax_tree:
                try:
                    show_tree(config.syntax_tree)
                except:
                    ColorPrints.print_in_red("Can Not Build The Syntax Tree!")
            
            if print_messages:
                if self.lexer_messages.errors == 0 and not self.compiled_failed:
                    ColorPrints.print_in_purple(f"No Lexer Error Found!")
                    self.lexer_messages.print_messages()

                elif self.lexer_messages.errors != 0 and not self.compiled_failed:
                    ColorPrints.print_in_red(f"{self.lexer_messages.errors} Lexer Errors Found!")
                    self.lexer_messages.print_messages()
                
               
                if self.parser_messages.errors == 0 and not self.compiled_failed:
                    ColorPrints.print_in_purple(f"No Parser Error Found!")
                    self.parser_messages.print_messages()

                elif self.parser_messages.errors != 0 and not self.compiled_failed:
                    ColorPrints.print_in_red(f"{self.parser_messages.errors} Parser Errors Found!")
                    self.parser_messages.print_messages()

           
            self.preprocess.visit(config.ast, None)
            self.type_checker.visit(config.ast, None)
           
            if print_messages:
                if self.semantic_messages.errors == 0 and not self.compiled_failed:
                    ColorPrints.print_in_purple(f"No Semantic Error Found!")
                    self.semantic_messages.print_messages()

                elif self.semantic_messages.errors != 0 and not self.compiled_failed:
                    ColorPrints.print_in_red(f"{self.semantic_messages.errors} Semantic Errors Found!")
                    self.semantic_messages.print_messages()
            
           
            if self.lexer_messages.errors == 0 and self.parser_messages.errors == 0 and self.semantic_messages.errors == 0:
                self.iR_generator.visit(config.ast, None)
                
                f = open(f"{os.path.join(os.getcwd(), 'generated_IR.out')}", "w")
                f.write(config.iR_code)
                f.close()


                ColorPrints.print_in_purple("TSLANG Terminal")
                self.run_tsvm.run()

        except:
            self.compiled_failed = True

        if self.compiled_failed:
            ColorPrints.print_in_red("Compile Failed!!!!!!")



class CompilerMessages(object):
    def __init__(self):
        self.errors = 0
        self.warnings = 0
        self.messages = []


    def print_messages(self):
        self.messages.sort(key=self.sort_by_lineno)
        for msg in self.messages:
            ColorPrints.print_in_black(f"{config.code_file_path}:", end="")
            ColorPrints.print_in_cyan(f"{msg['lineno']}: ", end="")
            if "is_warning" in msg:
                ColorPrints.print_in_yellow(f"{msg['message']}")
            else:
                ColorPrints.print_in_red(f"{msg['message']}")


    def add_message(self, message):
        if not message in self.messages:
            self.messages.append(message)
            if not "is_warning" in message:
                self.errors += 1 
            else:
                message["message"] = "WARNING" + message["message"]
                self.warnings +=1

    def sort_by_lineno(self, msg):
        return msg["lineno"]
