import os
import config
from compile import Compiler


file_address = "C:\\Users\\pariya\\OneDrive\\Desktop\\New folder\\Testlang_compiler\\funcfail.tes"
file_not_found = False
try:
    with open(file_address) as f:
        data = f.read()
        config.code_file_path = os.path.abspath(file_address)
except:

    file_not_found = True

if not file_not_found:
    compiler = Compiler()
    compiler.compile(data, show_syntax_tree=True, print_messages=True)
else:
    print("Wrong Directory!")
