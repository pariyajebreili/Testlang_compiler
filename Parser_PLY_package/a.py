from ply.yacc import yacc

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

parser.parse(line, debug=True)