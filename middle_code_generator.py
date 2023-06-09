from ply.yacc import yacc

#------- LEXICAL ANALYZER -------
from ply.lex import lex

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

def t_COMMENT(t):
    r' \x23.*'
    pass

def t_IDEN(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if the identifier is a reserved keyword
    t.type = reserved.get(t.value, 'IDEN')
    return t

# A regular expression rule with some action code
def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)    
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # remove the quotes from the string value
    return t

def t_newline(t):
    r"\n+"
    #t.lexer.lineno += t.value.count("\n")
    t.lexer.lineno += len(t.value)
    #print(t.lexer.lineno)


# recognize illegal character
def t_error(t):
    print(
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

lexer = lex()    




#------- PARSER GENERATOR -------

label_count=0
temp_count=0

#Error flag
verity=True

#REGISTER
register={}

#Register counter
reg_count=0

#Label counter
label_counter=0

#IR code
ir_code=[]
temp_code=[]


#For save variable type
varList=[]

#For save Function type
functionList=[('vector', 'list', (('num', 'n'),)+()),('num', 'print',(('num', 'n'),)+()),('num', 'scan', ()),('', 'print', (('num', 'n'),)+()),('num', 'len',(('list', 'A'),)+())]

#For save return type
returnList=[]

#For save inputs
inputs=[]

#For save assignment
assignmentList=[]

def functionType(f):
    for i in range(0,len(functionList)):
        for j in range(0,len(f)):
            if(functionList[i][1]==inputs[j][0]):
                inputs[j]=(functionList[i][0],)+inputs[j]  
            for k in range(0,len(f[j][2])):
                if(f[j][2][k]==functionList[i][1]):
                    functionType(f[j][2][k])
    return
                

def p_program_single(p):
    '''
    prog : func
    '''
    p[0]=[p[1]]
    

def p_program_multiple(p):
    '''
    prog : func prog
    '''
    p[0]=[[p[1]],] + [p[2]]



def p_function(p):
    '''func : DEF type iden LPAREN flist RPAREN LBRACE body RBRACE'''
    temp1=temp_code+ ir_code
    ir_code.clear()
    ir_code.extend(temp1)
    ir_code.insert(0,f'proc {p[2]}:')
    ir_code.insert(0,'\n')
    temp_code.clear()
    for i in functionList:
        if(p[3] in i):
            print('Unauthorized definition of a function')
            global verity
            verity=False

    p[0]=(p[2],p[3],p[5],p[8])
    functionList.append((p[2],p[3],p[5]))
    varList.append((p[2],p[3]))
    for i in returnList:
        if(p[2]=='int'):
            if(p[1]!=i[0] and i[0]!='number' and i[0]!='num' ):
                print(f'{p[1]}!={i} : Illegal return type')
                verity=False
        elif (p[2]=='vector'):
            if(p[1]!=i[0]):
                print(f'{p[1]}!={i} : Illegal return type')
                verity=False

    for i in range(0,len(functionList)):
        for j in range(0,len(inputs)):
            if(functionList[i][1]==inputs[j][0]):
                inputs[j]=(functionList[i][0],)+inputs[j]


    for i in functionList:
        for j in inputs:
            if(i[1]==j[1]):
                t=0
                if(len(i[2])!=len(j[2])):
                    print(f'{i[1]}({i[2]}) != {j[2]} : Number of unauthorized inputs in the function')
                    verity=False
                    
                else:
                    for k in j[2]:
                        
                        if(k[0]!=i[2][t][0]):
                            for x in functionList:
                                if(k[0]==x[1]):
                                    if(i[2][t][0]!=x[0]):
                                        print(f'Illegal parameter!')
                                        verity=False

                            if(i[2][t][0]=='num' and k[0]!='number'):
                                if(k[0]=='vector'):
                                    print('Illegal parameter!')
                                    verity=False
                            elif(i[2][t][0]=='vector'):
                                if(k[0]=='num' or k[0]=='number'):
                                    print('Illegal parameter!')
                                    verity=False
                        t+=1
                    




    for i in functionList:
        for j in assignmentList:
            if(i[1]==j[1]):
                if(i[0]!=j[0][0]):
                    print(f'{j[0]} = {(i[0],i[1])} : illegal assignment!')
                    verity=False
    
    varList.clear()
    returnList.clear()



def p_body_function(p):
    '''
    body : stmt 
         | stmt body
    '''
    if(len(p)==2):
        p[0]=(p[1])
    else:
        p[0]=(p[1])+p[2]

    



def p_statement(p):
    '''
    stmt : expr SEMI_COLON
         | defvar SEMI_COLON
         | IF LPAREN expr RPAREN stmt
         | IF LPAREN expr RPAREN stmt ELSE stmt
         | WHILE LPAREN expr RPAREN stmt
         | FOR LPAREN expr TO expr RPAREN stmt
         | RETURN expr SEMI_COLON
         | LBRACE body RBRACE
    '''

    global verity
    global reg_count;
    global label_count;
    if(len(p)==3):
        if(p[2]==';'):
            p[0]=p[1]
    elif (len(p)==4):
        if(p[3]==';'):
            p[0]=(p[1],p[2])

            if(p[1]=='return'):
                if(p[2]!=None):
                    if(type(p[2][1])==tuple):
                        if(p[2][1][0]=='number'):
                            temp_code.insert(len(temp_code),f'\tmov r0, -{p[2][1][1]} \n\tret')
                        if(p[2][1][0]=='num'):
                            temp_code.insert(len(temp_code),f'\tmul {register[p[2][1][1]]}, {register[p[2][1][1]]}, -1 \n\tmov r0, {register[p[2][1][1]]} \n\tret')
                        returnList.append(p[2][1])
                    elif (type(p[2][1])!=tuple):
                        returnList.append(p[2])
                        if(p[2][0]=='number'):
                            temp_code.insert(len(temp_code),f'\tmov r0, {p[2][1]} \n\tret')
                        elif(p[2][0]=='num'):
                            temp_code.insert(len(temp_code),f'\tmov r0, {register[p[2][1]]} \n\tret')


        else:
            p[0]=p[2]
    elif (len(p)==6):
        if(p[1]=='if'):
            if(p[3][1]=='=='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'\tlabel {label_count}:')
            elif(p[3][1]=='>='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
            elif(p[3][1]=='>'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
            elif(p[3][1]=='<='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
            elif(p[3][1]=='<'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-1,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
                    temp_code.insert(len(temp_code),f'label {label_count}:')

            p[0]=((p[1],(p[3])))+(p[5],)
        elif(p[1]=='while'):
            p[0]=((p[1],(p[3])))+(p[5],)
            level=0
            for i in p[5]:
                if(i=='if'):
                    level+=2
                elif(type(i) is tuple):
                    for j in i:
                        if(j in ['+','-','=','*']):
                            level+=1
            level=-level-1
            label_count=label_count+1
            temp_code.insert(level,f'label {label_count}:')
            if(p[3][1]=='=='):
                reg_count=reg_count+1
                label_count=label_count+1
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(level,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(level,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='>='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(level,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(level,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='>'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(level,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(level,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='<='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(level,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(level,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='<'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(level,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(level,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            temp_code.append(f'\tjmp label {label_count-1}')       
            temp_code.append(f'label {label_count}:')

    elif (len(p)==8):
        if(p[1]=='if'):
            p[0]=((p[1],(p[3])),)+(p[5],)+(p[6],)+(p[7],)
            if(p[3][1]=='=='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')

                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='>='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp>= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='>'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')

                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp > r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='<='):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp<= r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            elif(p[3][1]=='<'):
                reg_count=reg_count+1
                label_count=label_count+1;
                if(p[3][0][0]=='num' and p[3][2][0]=='num'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {register[p[3][2][1]]} \n\tjz r{reg_count}, label {label_count}')
                elif(p[3][2][0]=='number'):
                    temp_code.insert(len(temp_code)-2,f'\tcmp< r{reg_count}, {register[p[3][0][1]]}, {p[3][2][1]} \n\tjz r{reg_count}, label {label_count}')
            temp_code.insert(len(temp_code)-1,f'label {label_count}')


        elif (p[1]=='for'):
            p[0]=((p[1],p[3],p[4],(p[5])),)+(p[7],)
            level=0
            for i in p[7]:
                if(i=='if'):
                    level+=2
                elif(type(i) is tuple):
                    for j in i:
                        if(j in ['+','-','=','*']):
                            level+=1
            level=-level-1
            reg_count=reg_count+2
            label_count=label_count+2
            temp_code.insert(level,f'\tcall listlen, r{reg_count-1}, {register[p[5][1]]}\n\tmov r{reg_count}, {register[p[5][1]]}\nlabel {label_count-1}:')
            temp_code.insert(level,f'\tjz r{reg_count-1}, label {label_count}')
            temp_code.insert(level,f'\tsub r{reg_count-1}, r{reg_count-1}, 1')
            temp_code.append(f'\tadd r{reg_count}, r{reg_count}, 1')
            temp_code.append(f'\tjmp label {label_count-1}')
            temp_code.append(f'label {label_count}:')

        
def p_define_expression(p):
    '''
    expr : iden LPAREN clist RPAREN
         | expr LSQUAREBR expr RSQUAREBR
         | expr EQ expr
         | expr PLUS expr
         | expr MINUS expr
         | expr TIMES expr
         | expr DIVIDE expr
         | expr MOD expr
         | expr LESS_THAN expr
         | expr GREATER_THAN expr
         | expr PARITY expr
         | expr NOT_EQ expr
         | expr LESS_EQUAL expr
         | expr GREATER_EQUAL expr
         | expr OR expr
         | expr AND expr
         | NOT expr
         | MINUS expr
         | PLUS expr
         | LPAREN expr RPAREN
         | iden
         | num
    '''
    accu=False
    global verity
    global reg_count
    if(len(p)==2):
        p[0]=p[1]
        if(len(p[1])==1):
            for i in varList:
                if(p[0] in i[1]):
                    p[0]=i
                    accu=True
                    break 
            if(accu==False):
                print(f'{p[0]} : This variable is not defined') 
                verity=False
            else:
                accu=False
        if(type(p[1])==str):
            for i in varList:
                if(p[0] in i):
                    p[0]=i
                    accu=True
                    break

    elif (len(p)==3):
        if(p[1]=='+'):
            if(p[2][0]!='num' and p[2][0]!='number'):
                print(f'{p[0]} {p[1]} {p[2]} : Incompatible operands!')
                verity=False
        if(p[1]=='-'):

            if(p[2][0]!='num' and p[2][0]!='number'):
                print(f'{p[0]} {p[1]} {p[2]} : Incompatible operands!')
                verity=False
        if(p[1]=='!'):
            if(p[2][0]!='num' or p[2][0]!='number'):
                print(f'{p[1]} {p[2]} : Incompatible operands!')
                verity=False
        p[0]=(p[1],p[2])

    elif (len(p)==4):
        p[0]=(p[1],p[2],p[3])
        if(p[2]=='+'):
            if(p[1][1]=='['):
                reg_count=reg_count+1
                if(p[1][2][0]=='number'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][0][1]]}, {p[1][2][1]*8}')
                    reg_count=reg_count+1
                    if(p[3][0]=='number'):
                        temp_code.append(f'\tld r{reg_count}, r{reg_count-1}')
                    elif(p[3][0]=='num'):
                        temp_code.append(f'\tld r{reg_count}, r{reg_count-1}')
                elif(p[1][2][0]=='num'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][0][1]]}, {register[p[1][2][1]]}')
                    reg_count=reg_count+1
                    if(p[3][0]=='number'):
                        temp_code.append(f'\tld r{reg_count}, r{reg_count-1}')
                    elif(p[3][0]=='num'):
                        temp_code.append(f'\tld r{reg_count}, r{reg_count-1}')

            if(len(p[1])==2):
                reg_count=reg_count+1
                if(p[1][0]=='num' and p[3][0]=='num'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][1]]}, {register[p[3][1]]}')
                elif(p[1][0]=='num' and p[3][0]=='number'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][1]]}, {p[3][1]}')
                elif(p[1][0]=='number' and p[3][0]=='num'):
                    temp_code.append(f'\tadd r{reg_count}, {p[1][1]}, {register[p[3][1]]}')
                elif(p[1][0]=='number' and p[3][0]=='number'):
                    temp_code.append(f'\tadd r{reg_count}, {p[1][1]}, {p[3][1]}')
            else:
                reg_count=reg_count+1
                if( p[3][0]=='num'):
                    temp_code.append(f'\tadd r{reg_count}, r{reg_count-1}, {register[p[3][1]]}')
                elif(p[3][0]=='number'):
                    temp_code.append(f'\tadd r{reg_count}, r{reg_count-1}, {p[3][1]}')
                
                


            if(len(p[1])==2 and len(p[3])==2):
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False
                    return
                else:
                    p[0]=(p[1][0],p[1],p[2],p[3])
            else:
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False


        if(p[2]=='-'):
            if(p[1][1]=='['):
                reg_count=reg_count+1
                if(p[1][2][0]=='number'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][0][1]]}, {p[1][2][1]*8}')
                    reg_count=reg_count+1
                    temp_code.append(f'\tld r{reg_count}, {reg_count-1} ')
                elif(p[1][2][0]=='num'):
                    temp_code.append(f'\tadd r{reg_count}, {register[p[1][0][1]]}, {register[p[1][2][1]]}')
                    reg_count=reg_count+1
                    temp_code.append(f'\tld r{reg_count}, {reg_count-1} ')

            if(len(p[1])==2):
                reg_count=reg_count+1
                if(p[1][0]=='num' and p[3][0]=='num'):
                    temp_code.append(f'\tsub r{reg_count}, {register[p[1][1]]}, {register[p[3][1]]}')
                elif(p[1][0]=='num' and p[3][0]=='number'):
                    temp_code.append(f'\tsub r{reg_count}, {register[p[1][1]]}, {p[3][1]}')
                elif(p[1][0]=='number' and p[3][0]=='num'):
                    temp_code.append(f'\tsub r{reg_count}, {p[1][1]}, {register[p[3][1]]}')
                elif(p[1][0]=='number' and p[3][0]=='number'):
                    temp_code.append(f'\tsub r{reg_count}, {p[1][1]}, {p[3][1]}')
            else:
                reg_count=reg_count+1
                if( p[3][0]=='num'):
                    temp_code.append(f'\tsub r{reg_count}, r{reg_count-1}, {register[p[3][1]]}')
                elif(p[3][0]=='number'):
                    temp_code.append(f'\tsub r{reg_count}, r{reg_count-1}, {p[3][1]}')


            if(len(p[1])==2 and len(p[3])==2):
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False
                else:
                    p[0]=(p[1][0],p[1],p[2],p[3])
            else:
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False

        if(p[2]=='*'):
            if(len(p[1])==2 and len(p[3])==2):
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False
                else:
                    p[0]=(p[1][0],p[1],p[2],p[3])
            else:
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False

        if(p[2]=='/'):
            if(len(p[1])==2 and len(p[3])==2):
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False
                else:
                    p[0]=(p[1][0],p[1],p[2],p[3])
            else:
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False

        if(p[2]=='%'):
            if(len(p[1])==2 and len(p[3])==2):
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False
                else:
                    p[0]=(p[1][0],p[1],p[2],p[3])
            else:
                if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                    print(f'{p[1]} {p[2]} {p[3]} : Incompatible operands!')
                    verity=False

        if(p[2]=='='):
            if(p[1]!=None and p[3]!=None):
                if(p[1][1]=='['):
                    if(p[1][2][0]=='number'):
                        if(len(p[3])==2):
                            reg_count=reg_count+2
                            temp_string=f'\tadd r{reg_count}, {register[p[1][0][1]]}, {p[1][2][1]*8}\n\tmov r{reg_count-1}, {p[3][1]}\n\tst r{reg_count-1}, r{reg_count}'
                        else:
                            reg_count=reg_count+1
                            temp_string=f'\tadd r{reg_count}, {register[p[1][0][1]]}, {p[1][2][1]*8}\n\tst r{reg_count-1}, r{reg_count}'
                        temp_code.append(temp_string)
                    elif(p[1][2][0]=='num'):
                        #I have to fix array's value (index*8)
                        if(len(p[3])==2):
                            reg_count=reg_count+2
                            temp_string=f'\tmul r{reg_count-1}, {register[p[1][2][1]]}, 8\n\tadd r{reg_count}, {register[p[1][0][1]]}, r{reg_count-1}\n\tmov r{reg_count-1}, r{register[p[3][1]]}\n\tst r{reg_count-2}, r{reg_count}'
                        else:
                            reg_count=reg_count+2
                            temp_string=f'\tmul r{reg_count-1}, {register[p[1][2][1]]}, 8\n\tadd r{reg_count}, {register[p[1][0][1]]}, r{reg_count-1}\n\tst r{reg_count-2}, r{reg_count}'
                        temp_code.append(temp_string)

                if(len(p[1])==2 and len(p[3])>=2 and p[3][1]!='('):
                    if(len(p[0][2])==2):
                        if(p[0][2][0]=='number'):
                            temp_code.append(f'\tmov {register[p[0][0][1]]}, {p[0][2][1]}')
                        elif(p[0][2][0]=='num'):
                            temp_code.append(f'\tmov {register[p[0][0][1]]}, {register[p[0][2][1]]}')
                        elif(p[0][2][0]=='list'):
                            temp_code.append(f'\tmov {register[p[0][0][1]]}, {register[p[0][2][1]]}')
                    elif(len(p[0][2])==4):
                        if(p[0][2][2]=='+'):
                            #temp_code.pop()
                            if(p[0][2][1][0]=='num'):
                                temp_code.append(f'\tadd {register[p[0][0][1]]}, {register[p[0][2][1][1]]}, {p[0][2][3][1]}')
                            elif(p[0][2][3][0]=='num'):
                                temp_code.append(f'\tadd {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {p[0][2][1][1]}')
                            else:
                                temp_code.append(f'\tadd {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {register[p[0][2][1][1]]}')                

                        if(p[0][2][2]=='-'):
                            temp_code.pop()
                            if(p[0][2][1][0]=='num'):
                                temp_code.append(f'\tsub {register[p[0][0][1]]}, {register[p[0][2][1][1]]}, {p[0][2][3][1]}')
                            elif(p[0][2][3][0]=='num'):
                                temp_code.append(f'\tsub {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {p[0][2][1][1]}')
                            else:
                                temp_code.append(f'\tsub {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {register[p[0][2][1][1]]}')                

                        if(p[0][2][2]=='*'):
                            if(p[0][2][1][0]=='num'):
                                temp_code.append(f'\tmul {register[p[0][0][1]]}, {register[p[0][2][1][1]]}, {p[0][2][3][1]}')
                            elif(p[0][2][3][0]=='num'):
                                temp_code.append(f'\tmul {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {p[0][2][1][1]}')
                            else:
                                temp_code.append(f'\tmul {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {register[p[0][2][1][1]]}')                

                        if(p[0][2][2]=='/'):
                            if(p[0][2][1][0]=='num'):
                                temp_code.append(f'\tdiv {register[p[0][0][1]]}, {register[p[0][2][1][1]]}, {p[0][2][3][1]}')
                            elif(p[0][2][3][0]=='num'):
                                temp_code.append(f'\tdiv {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {p[0][2][1][1]}')
                            else:
                                temp_code.append(f'\tdiv {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {register[p[0][2][1][1]]}')                

                        if(p[0][2][2]=='%'):
                            if(p[0][2][1][0]=='num'):
                                temp_code.append(f'\tmod {register[p[0][0][1]]}, {register[p[0][2][1][1]]}, {p[0][2][3][1]}')
                            elif(p[0][2][3][0]=='num'):
                                temp_code.append(f'\tmod {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {p[0][2][1][1]}')
                            else:
                                temp_code.append(f'mod {register[p[0][0][1]]}, {register[p[0][2][3][1]]}, {register[p[0][2][1][1]]}')                
                    else:
                        temp_code.append(f'\tmov {register[p[0][0][1]]}, r{reg_count}')


                    if(p[1][0]=='number'):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
                    if(p[1][0]!=p[3][0]):
                        if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                            print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                            verity=False
                if(p[3][1]=='('):
                    temp_code.pop()
                    assignmentList.append((p[1],p[3][0]))
                    p[3]=(p[3][0],p[3][2])
                    p[0]=(p[1],p[2],p[3])
                    if(p[0][2][0]=='makeList'):

                        temp_code.append(f'\tmov {register[p[0][0][1]]}, {p[0][2][1][0][1]} \n\tcall mem, {register[p[0][0][1]]}')
                    elif(p[0][2][0]=='numread'):
                        temp_code.append(f'\tcall iget, {register[p[0][0][1]]}')
                    else:
                        temp_string=f'\tcall {p[0][2][0]}, {register[p[0][0][1]]}'
                        if(len(p[3][1])>0):
                            for i in p[3][1]:
                                if(i[0]=='num'):
                                    temp_string=temp_string+f', {register[i[1]]}'
                                elif(i[0]=='list'):
                                    temp_string=temp_string+f', {register[i[1]]}'
                                elif(i[0]=='number'):
                                    temp_string=temp_string+f', {i[1]}'
                            temp_code.append(temp_string)
                        
        if(p[2]=='<'):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0]):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
        if(p[2]=='<='):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0]):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
        if(p[2]=='>'):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0]):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
        if(p[2]=='>='):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0]):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
        if(p[2]=='=='):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0] and ((p[1][0]=='num' and p[3][0]=='list') or(p[1][0]=='list' and p[3][0]=='num')) ):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
        if(p[2]=='!='):
            if(p[1]!=None and p[3]!=None):
                if(len(p[1])==2 and len(p[3])==2):
                    if(p[1][0]!=p[3][0]):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
    elif (len(p)==5):
        
        if(p[2]=='('):
            if(p[1]!=None):
                find_function=False
                for k in functionList:
                    if(k[1]==p[1]):
                        find_function=True
                if(find_function != True):
                    print(f'{p[1]} : This function is not defined.')
                    verity=False
                inputs.append((p[1],p[3]))
                p[0]=(p[1],p[2],p[3],p[4])
                temp_string=f''
                if(p[0][0]=='numprint'):
                    #very sensetive
                    if(temp_code[len(temp_code)-1]==''):
                        temp_code.pop()
                    for i in functionList:
                        if(p[0][2][0][0] in i):
                            temp_string=f'\tcall iput, {register[i[2][0][1]]}'
                            break
                    if(temp_string==f''):
                        if(p[0][2][0]=='number'):
                            reg_count=reg_count+1
                            register[p[0][2][1]]=f'r{reg_count}'
                            temp_string=f'\tcall iput, {register[p[0][2][1]]}'
                    temp_code.append(temp_string)
                else:
                    temp_string=f'\tcall {p[0][0]}'
                    if(len(p[3])>0):
                        for i in p[3]:
                                if(i[0]=='num'):
                                    temp_string=temp_string+f', {register[i[1]]}'
                                elif(i[0]=='list'):
                                    temp_string=temp_string+f', {register[i[1]]}'
                                elif(i[0]=='number'):
                                    temp_string=temp_string+f', {i[1]}'
                        temp_code.append(temp_string)

        if(p[2]=='['):
            if(p[1]!=None):
                p[0]=(p[1],p[2],p[3],p[4])
                # if(p[3][0]=='number'):
                #     reg_count=reg_count+1
                #     temp_string=f'\tadd r{reg_count},{register[p[1][1]]}, {p[3][1]}'
                #     temp_code.append(temp_string)
            





def p_variable_multiple(p):
    '''
    flist : type iden
          | type iden COMMA flist
          |
    '''
    global register
    global reg_count
    reg_count = reg_count+1
    if(len(p)==3):
        varList.append((p[1],p[2]))
        p[0]=(p[1],p[2])
        p[0]=()+(p[0],)
        register[p[2]]=f'r{reg_count}'
    elif (len(p)==5):
        varList.append((p[1],p[2]))
        p[0]=(p[1],p[2])
        p[0]=()+(p[0],)+p[4]
        register[p[2]]=f'r{reg_count}'
    else:
        p[0]=()
    # if(len(p[0])>0):
    #     print(p[0])


def p_variable_array(p):
    '''
    clist : expr 
          | expr COMMA clist
          |
    '''
    if(len(p)==2):
        p[0]=(p[1])
        p[0]=(p[0],)+()
    elif (len(p)==4):
        p[0]=(p[1],)+p[3]
    else:
        p[0]=()


def p_define_variable(p):
    '''defvar : VAR type iden'''
    global verity
    p[0]=(p[2],p[3])
    for i in varList:
        if(p[3] in i):
            print('Duplicate variable error')
            verity=False
    varList.append((p[2],p[3]))
    global reg_count
    global register
    reg_count=reg_count+1
    register[p[3]]=f'r{reg_count}'


#def p_define_variable(p):
#    '''defvar : VAR type iden EQ expr'''
#    global verity
#    p[0] = (p[2], p[3], p[5])
#    for i in varList:
#        if p[3] in i:
#            print('Duplicate variable error')
#            verity = False
#    varList.append((p[2], p[3], p[5]))
#    global reg_count
#    global register
#    reg_count += 1
#    register[p[3]] = f'r{reg_count}'



def p_variabel_type(p):
    '''
    type : INT 
         | VECTOR
         | NULL
    '''
    p[0]=p[1]


def p_expr_num(p):
    '''
    num : NUM
    '''
    p[0]=('number',p[1])


def p_expr_iden(p):
    '''
    iden : IDEN
    '''
    p[0]=(p[1])


#def p_empty(p):
#    '''empty :'''
#    pass


# Utilize File
file = open("C:\\Users\\pariya\\OneDrive\\Desktop\\testlang_compiler\\for.tes")

line = file.read()
file.close()
# print(line)

def p_error(p):
   if p:
        print("Syntax error at token", p.type)
        print("Syntax error at '%s'" % p.value)
        print("line : '%s'" % p.lineno)
        #print("Syntax error in input!")
        #parser.errok()
        # print(p.lexer.skip(1))
   else:
       print("Syntax error at EOF")


parser=yacc()

parser.parse(line)

#------- Generate middle code -------
if(verity==True):
    for i in ir_code:
        print(i)