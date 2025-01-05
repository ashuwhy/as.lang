# AS Programming Language Explained

## Overview
AS is a lightweight programming language implemented in Python, designed for simplicity and ease of use. It features a custom syntax that combines elements from Python and JavaScript while maintaining readability.

## Core Components

### 1. Lexer (`as_lexer.py`)
The lexer breaks down source code into tokens using the SLY library. It handles:
- Keywords (`if`, `else`, `while`, etc.)
- Operators (`+`, `-`, `*`, `/`, etc.)
- Numbers and strings
- Comments (starting with `//`)
- Variable names
- Special symbols (`{}`, `[]`, `()`)

### 2. Parser (`as_parser.py`)
The parser converts tokens into an Abstract Syntax Tree (AST) using grammar rules. Key features:
- Expression parsing
- Statement handling
- Operator precedence
- Control flow structures

### 3. Executor (`executor.py`)
The executor walks through the AST and executes the code. It handles:
- Variable management
- Expression evaluation
- Control flow execution
- Built-in functions
- Error handling

## Language Features

### 1. Variables and Data Types
```javascript
x = 5                  // Numbers
name = "John"          // Strings
numbers = [1, 2, 3]    // Lists
```

### 2. Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `^`
- Comparison: `==`, `!=`, `>`, `>=`, `<`, `<=`
- Logical: `and`, `or`
- Increment/Decrement: `inc`, `dec`

### 3. Control Structures
```javascript
// If-else statements
if condition {
    statement
} else {
    statement
}

// While loops
while condition 
do {
    statement
}
```

### 4. Input/Output
```javascript
// Output
output "Hello, World!"

// Input
name = input "Enter your name: "
```

### 5. Comments
```javascript
// This is a single-line comment
```

## Implementation Details

### Project Structure
```
aslang/
├── __init__.py         # Version and metadata
├── __main__.py         # Entry point
├── as_lexer.py        # Tokenization
├── as_parser.py       # Parsing
└── executor.py        # Execution engine
```

### Execution Flow
1. Source code is read
2. Lexer breaks it into tokens
3. Parser creates AST
4. Executor walks through AST
5. Results are output

### Error Handling
The language provides friendly error messages:
- Undefined variables: "as says: {variable} hasn't been defined!"
- Type errors: "as says: You can't use '{op}' with types '{type1}' and '{type2}'"
- Index errors: "as says: index out of range"

## Usage

### Installation
```bash
pip install as
```

### Running Programs
```bash
# Run a file
python -m aslang filename.as

# Interactive shell
python -m aslang
```

## Technical Implementation Notes

1. **Lexical Analysis**
   - Uses SLY (Sly Lex Yacc) for lexing
   - Defines token patterns using regular expressions
   - Handles whitespace and comments

2. **Parsing**
   - Implements recursive descent parsing
   - Builds AST using grammar rules
   - Maintains operator precedence

3. **Execution**
   - Uses recursive evaluation of AST nodes
   - Maintains global variable scope
   - Implements built-in functions

## Design Philosophy
- Simplicity over complexity
- Readable syntax
- Friendly error messages
- Easy to learn and use
- Python-like semantics with JavaScript-like syntax

## Limitations
- Single global scope
- Limited data types
- No functions/procedures
- No object-oriented features
- Basic error handling

This language serves as an excellent example of how to implement a simple programming language and demonstrates core concepts of language design and implementation. 