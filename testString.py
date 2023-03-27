import ply.lex as lex

# Define token names
tokens = [
    'STRING'
]

# Define states for handling string literals
states = (
    ('str', 'exclusive'),
)

# Define a rule to handle string literals in the 'str' state
def t_str_STRING(t):
    r'"'
    t.lexer.push_state('str')
    t.lexer.string = ""
    return None

# Define a rule to handle string literals in the 'str' start state
def t_str_strcont(t):
    r'(?:(?<=\\)[\\"nrt]|(?<!\\)"[^"]*")'
    t.lexer.string += t.value
    if not t.value.endswith("\\"):
        t.lexer.pop_state()
        t.value = t.lexer.string[1:-1].replace(r'\"', '"').replace(r"\\", "\\")
        return t

# Define a function to handle unmatched characters in the 'str' state
def t_str_error(t):
    print(f"Invalid character in string literal: {t.value[0]}")
    t.lexer.skip(1)

# Define a rule to ignore whitespace outside of string literals
def t_WHITESPACE(t):
    r'\s+'
    pass

# Define an error handling rule for unmatched characters outside of string literals
def t_error(t):
    print(f"Invalid character outside of string literal: {t.value[0]}")
    t.lexer.skip(1)

# Create lexer
lexer = lex.lex()

# Test lexer
text = 'x = "hello world" y = "my name is \\"Alice\\"! How do you do?"'
lexer.input(text)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value)