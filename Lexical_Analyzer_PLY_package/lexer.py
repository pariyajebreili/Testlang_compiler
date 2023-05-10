from ply.lex import lex

class Lexer(object):
    
    def __init__(self, tokens):
        #lexer=lex()
        self.lexer = lex(object=tokens)        

    def build(self, data):
        #data = "C:\\Users\\pariya\\OneDrive\\Desktop\\testlang-compiler\\testgrammer.tes"
        self.lexer.input(data)
        for tok in self.lexer:
            print(tok.value, tok.type)
