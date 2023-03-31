from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'VOID','FOR','IF','ELSE','RETURN','WHILE','PRINT','IN','NUM','INT','DEF','VAR','IN','AND','OR','TRUE','FALSE',}
    token_specification = [
        ('NUMBER',   r'[0-9]+'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),   
        ('LPAREN',   r'\('),   
        ('RPAREN',   r'\)'),    
        ('LSQUAREBR',r'\['),
        ('RSQUAREBR',r'\]'),  
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character

    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
def int sum(vector numList) {
var int result = 0;
for (i = 0 to length(numList)) {
result = result + numList[i];
# this is comment
}
return result;
'''

for token in tokenize(statements):
    print(token)