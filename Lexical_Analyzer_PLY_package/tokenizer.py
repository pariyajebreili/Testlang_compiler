from ply.lex import lex
from ply.lex import TOKEN

# Define states for handling string literals
states = (
    ('STR', 'inclusive'),
)

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
    'in':    'IN',
    'and':   'AND',
    'or':    'OR',
    'true':  'TRUE',
    'false': 'FALSE',
}

#--Tokens--
tokens=[
    'NUMBER','VECTOR','COMMENT','STR',
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

# Define a lexer rule for the STRING token
#string_literal_patter=r'(\"[^\"]*\"|\'[^\']*\')'
#@TOKEN(string_literal_patter)
#def t_STR(t):
#    return t


def t_STR(t):
    r'[\"\']'
    t.lexer.begin('STR')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value


def t_STR_chars(t):
    r'[^"\'\n]+'


def t_STR_newline(t):
    r'\n+'
    print("Incorrectly terminated string %s" % t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1])
    t.lexer.skip(1)


def t_STR_end(t):
    r'[\"\']'

    if t.lexer.str_marker == t.value:
        t.type = 'STR'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        t.lexer.begin('INITIAL')
        return t



#ignore Tab and enter
t_VECTOR = r'\[[^\]]*\]'
t_ignore=' \t \n' 

def t_COMMENT(t):
    r' \#.*'
    pass


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if the identifier is a reserved keyword
    t.type = reserved.get(t.value, 'ID')
    return t

 # A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+'
    #r'[0-9]+'
    if ("." in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)    
    return t



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

