# testlang_compiler

This is a compiler for a testlang programming language that generates executable code for a target machine. The compiler takes source code written in the testlang language and that can be executed on the target system.

## Getting Started

To use the compiler, you need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can clone the repository from GitHub and run the compiler using the following command:

```
python main.py 
```

`file_address` in `main.py` is the path to the source code file you want to compile.

## Language Features

The testlang supported by the compiler includes the following features:

- Variables and data types (integer, etc.)
- Arithmetic and logical expressions
- Control flow statements (if-else, while, for, etc.)
- Functions and procedures


## Architecture

1. **Lexical Analysis**: The source code is tokenized into a sequence of lexemes by the lexer, which identifies the basic building blocks of the language, such as keywords, identifiers, and literals.

2. **Syntax Analysis**: The parser reads the sequence of lexemes and constructs a parse tree that represents the structure of the program according to the language grammar rules.

3. **Semantic Analysis**: The semantic analyzer checks the program for semantic errors, such as type mismatches and undeclared variables. It also performs type checking and generates symbol tables.

4. **IR Generation**: The IR generator traverses the parse tree and generates IR code that corresponds to the program's semantics and can be executed on the target machine.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
