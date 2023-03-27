from ply.lex import lex


# Define states for handling string literals
#states = (
#    ('STR', 'exclusive'),
#)
#--reserved--
reserved = {
    'void': 'VOID',
    'for' : 'FOR',
    'if' : 'IF',
    'else' : 'ELSE',
    'return': 'RETURN',
    'while': 'WHILE',
    'print':'PRINT',
    'in':'IN',
    'num':'NUM',
    'int': 'INT',
    'def':'DEF',
    'var':'VAR',
    'float': 'FLOAT',
}

#--Tokens--
tokens=[
    'NUMBER','VECTOR',
    # Operators
    'PLUS','TIMES','DIVIDE','MOD','MINUS',
    # Delimeters
    'LPAREN','RPAREN','LBRACE','RBRACE','LSQUAREBR','RSQUAREBR','COLON','COMMA','SEMI_COLON',
    # Logical Operators
    'LESS_THAN','LESS_EQUAL','GREATER_THAN','GREATER_EQUAL','EQ','NOT_EQ','PARITY','NOT',
]+ list(reserved.values())+ ['ID']




t_PLUS=r'\+'
t_MINUS=r'\-'
t_TIMES=r'\*'
t_DIVIDE=r'\/'
t_MOD=r'%'
t_LPAREN  = r'\('
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


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if the identifier is a reserved keyword
    t.type = reserved.get(t.value, 'ID')
    return t


 # A regular expression rule with some action code
def t_NUMBER(t):
    r'(\d)+(\.(\d)+)?'
    #r'[0-9]+'
    if ("." in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)    
    return t

t_VECTOR = r'\[[^\]]*\]'


#ignore Tab and enter
t_ignore=' \t \n' 

# recognize illegal character
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


lexer=lex()
newlexer = lexer.clone()

file = open("testlang.txt")
line = file.read()
file.close()

if __name__ == "__main__":
    lexer.input(line)
    newlexer.input(line)

    for tok in lexer:
        print(tok.type,tok.value)

    #for tok in newlexer:
    #    print(tok)

