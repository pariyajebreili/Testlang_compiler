from ply.lex import lex

class Tokens(object):


    def __init__(self, lexer_messages):
        self.lexer_messages = lexer_messages

    #--reserved--
    reserved = {
        'for' : 'FOR',
        'if' : 'IF',
        'else' : 'ELSE',
        'return': 'RETURN',
        'while': 'WHILE',
        'to':'TO',
        'int': 'INT',
        'def':'DEF',
        'var':'VAR',
        'and': 'AND',
        'or':  'OR',
        'vector':'VECTOR',
        'null':'NULL',
       
    }

    #--Tokens--
    tokens=[
        'NUM','IDEN','STRING',
        # Operators
        'PLUS','TIMES','DIVIDE','MOD','MINUS',
        # Delimeters
        'LPAREN','RPAREN','LBRACE','RBRACE','LSQUAREBR','RSQUAREBR','COLON','COMMA','SEMI_COLON',
        # Logical Operators
        'LESS_THAN','LESS_EQUAL','GREATER_THAN','GREATER_EQUAL','EQ','NOT_EQ','PARITY','NOT','QMARK',
    ]+ list(reserved.values())



    t_QMARK = r'\?'
    t_PLUS=r'\+'
    t_MINUS=r'\-'
    t_TIMES=r'\*'
    t_DIVIDE=r'\/'
    t_MOD=r'%'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE=r'\{'
    t_RBRACE=r'\}'
    t_LSQUAREBR=r'\['
    t_RSQUAREBR=r'\]'
    t_COLON=r':'
    t_COMMA=r','
    t_SEMI_COLON=r';'
    t_LESS_THAN=r'\<'
    t_LESS_EQUAL=r'\<\='
    t_GREATER_THAN=r'>'
    t_GREATER_EQUAL=r'>='
    t_EQ=r'='
    t_NOT_EQ=r'\!\='
    t_PARITY=r'\=\='
    t_NOT=r'\!'


    #ignore Tab and enter
    t_ignore = ' \t'

    def t_COMMENT(self, t):
        r' \x23.*'
        pass

    def t_IDEN(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        # Check if the identifier is a reserved keyword
        t.type = self.reserved.get(t.value, 'IDEN')
        return t

    # A regular expression rule with some action code
    def t_NUM(self,t):
        r'[0-9]+'
        t.value = int(t.value)    
        return t
    

    def t_STRING(self,t):
        r'"[^"]*"'
        t.value = t.value[1:-1]  # remove the quotes from the string value
        return t

    def t_newline(self, t):
        r"\n+"
        #t.lexer.lineno += t.value.count("\n")
        t.lexer.lineno += len(t.value)
        #print(t.lexer.lineno)
    
   
    # recognize illegal character
    def t_error(self, t):
        self.lexer_messages.add_message(
            {"message": f"Illegal character '{t.value[0]}'", "lineno": t.lexer.lineno})
        t.lexer.skip(1)


    precedence = (
        ('left', 'error'),
        ('left', 'AND', 'OR'),
        ('left', 'NOT', 'LESS_EQUAL', 'GREATER_EQUAL','NOT_EQ', 'PARITY', 'LESS_THAN', 'GREATER_THAN'),
        ('left', 'EQ', 'QMARK', 'COLON'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD'),
        ('left', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE')
    )

