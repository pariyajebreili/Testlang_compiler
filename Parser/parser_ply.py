from ply.lex import lex
from ply.yacc import yacc

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
    'to':'TO',
    'num':'NUM',
    'int': 'INT',
    'def':'DEF',
    'var':'VAR',
    'in':    'IN',
    'and':   'AND',
    'or':    'OR',
    'true':  'TRUE',
    'false': 'FALSE',
    'vector':'VECTOR',
    'type':'TYPE',
}

#--Tokens--
tokens=[
    'NUMBER','COMMENT','STR',
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


#------- PARSER GENERATOR -------
label_count=0
temp_count=0

#Error flag
verity=True

#For generate Label
def label():
    global label_count
    label_count +=1
    return f'label{label_count}'

#For generate temp
def register():
    global temp_count
    temp_count +=1
    return f'r{temp_count}'


#For save variable type
varList=[]

#For save Function type
functionList=[('vector', 'list', (('int', 'n'),)+()),('int', 'scan',(('int', 'n'),)+())]

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
    """
    prog : func prog
         | empty
    """
    if len(p) == 3:
        p[0]=[[p[1]],] + [p[2]]


def p_empty(p):
    "empty :"
    p[0] = []   


#def p_program_multiple(p):
#    '''
#    prog : func prog
#    '''
#    p[0]=[[p[1]],] + [p[2]]


def p_func(p):
    '''
    func : DEF TYPE ID LPAREN flist RPAREN LBRACE body RBRACE
    '''
    if p[1] == 'DEF':
        for i in functionList:
            if(p[2] in i):
                print('Unauthorized definition of a function')
                global verity
                verity=False

        p[0]=(p[2],p[3],p[5],p[8])
        functionList.append((p[2],p[3],p[5]))
        varList.append((p[2],p[3]))
        for i in returnList:
            if(p[2]=='int'):
                if(p[2]!=i[0] and i[0]!='number'):
                    print(f'{p[1]}!={i} : Illegal return type')
                    verity=False
            elif (p[2]=='list'):
                if(p[2]!=i[0]):
                    print(f'{p[2]}!={i} : Illegal return type')
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
                                    if(k[0]=='list'):
                                        print('Illegal parameter!')
                                        verity=False
                                elif(i[2][t][0]=='list'):
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
    else:
        print("this is error you should type def first")




def p_body_function(p):
    '''
    body : stmt 
         | stmt body
    '''
    if(len(p)==2):
        p[0]=(p[1])
    else:
        p[0]=(p[1])+p[2]
    
    


def p_stmt(p):
    '''
    stmt : expr SEMI_COLON
         | defvar SEMI_COLON
         | IF LPAREN expr RPAREN stmt
         | IF LPAREN expr RPAREN stmt ELSE stmt
         | WHILE LPAREN expr RPAREN stmt
         | FOR LPAREN ID TO expr RPAREN stmt
         | RETURN expr SEMI_COLON
         | LBRACE body RBRACE
    '''
    global verity
    if(len(p)==3):
        if(p[2]==';'):
            p[0]=p[1]
    elif (len(p)==4):
        if(p[3]==';'):
            p[0]=(p[1],p[2])
            if(p[1]=='return'):
                if(p[2]!=None):
                    if(type(p[2][1])==tuple):
                        returnList.append(p[2][1])
                    elif (type(p[2][1])!=tuple):
                        returnList.append(p[2])
        else:
            p[0]=p[2]
    elif (len(p)==6):
        if(p[1]=='if'):
            p[0]=((p[1],(p[3])))+(p[5],)
        elif(p[1]=='while'):
            p[0]=((p[1],(p[3])))+(p[5],)
    elif (len(p)==8):
        if(p[1]=='if'):
            p[0]=((p[1],(p[3])),)+(p[5],)+(p[6],)+(p[7],)
        elif (p[1]=='for'):
            p[0]=((p[1],p[3],p[4],(p[5])),)+(p[7],)
    elif (len(p)==2):
        p[0] = p[1]


def p_define_variable(p):
    '''
    defvar : VAR TYPE ID 
    '''
    global verity
    p[0]=(p[2],p[3])
    for i in varList:
        if(p[3] in i):
            print('Duplicate variable error')
            verity=False
    varList.append((p[2],p[3]))




def p_variable_multiple(p):
    '''
    flist : TYPE ID
          | TYPE ID COMMA flist
          |
    '''
    if(len(p)==3):
        varList.append((p[1],p[2]))
        p[0]=(p[1],p[2])
        p[0]=()+(p[0],)
    elif (len(p)==5):
        varList.append((p[1],p[2]))
        p[0]=(p[1],p[2])
        p[0]=()+(p[0],)+p[4]
    else:
        p[0]=()



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



        


def p_expr(p):
    '''
    expr : VAR LPAREN clist RPAREN
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
         | VAR
         | NUMBER
    '''
    accu=False
    global verity
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


        if(p[2]=='-'):
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
                if(len(p[1])==2 and len(p[3])>=2 and p[3][1]!='('):
                    if(p[1][0]=='number'):
                        print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                        verity=False
                    if(p[1][0]!=p[3][0]):
                        if((p[3][0]=='number' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='number') or (p[3][0]=='num' and p[1][0]=='list') or (p[3][0]=='list' and p[1][0]=='num')):
                            print(f'{p[1]} {p[2]} {p[3]} : Illegal assignment!')
                            verity=False
                if(p[3][1]=='('):
                    assignmentList.append((p[1],p[3][0]))
                    p[3]=(p[3][0],p[3][2])
                    p[0]=(p[1],p[2],p[3])

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
                    if(p[1][0]!=p[3][0]):
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
        if(p[2]=='['):
            if(p[1]!=None):
                p[0]=(p[1],p[2],p[3],p[4])
            






# Utilize File
file = open("C:\\Users\\pariya\\OneDrive\\Desktop\\testlang-compiler\\Parser_PLY_package\\testlang.txt")

line = file.read()
file.close()
print(line)

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


print(verity)