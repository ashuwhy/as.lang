# AS Programming Language

AS is a lightweight programming language implemented in Python, designed for simplicity and ease of use.

![Version](https://img.shields.io/badge/version-0.1-blue)

## Installation

You can install AS using one of the following methods:

**Stable Release:**
```bash
pip install as
```

**Development Version:**
```bash
pip install git+https://github.com/ashuwhy/aslang.git
```

## Usage

Run AS programs using:
```bash
python -m aslang [filename]
```
If no filename is provided, AS will start in interactive shell mode.

## Language Features

### Basic Syntax

**Hello World**
```javascript
output "Hello, World!"
```

### Variables

Variables are dynamically typed and created upon first assignment:

```javascript
x = 5
y = "Mark"
output x    // Displays: 5
output y    // Displays: Mark
```

> **Note:** Variable names are case-sensitive

### Arrays

AS supports multi-dimensional arrays (1D to 4D):

```javascript
// 1D Array
numbers = array[5]
numbers[0] = 10

// 2D Array
matrix = array[3][3]
matrix[0][0] = 1

// 3D Array
cube = array[2][2][2]
cube[0][0][0] = 1

// 4D Array
hypercube = array[2][2][2][2]
hypercube[0][0][0][0] = 1
```

Each array dimension is zero-indexed and supports both reading and writing operations. Arrays are initialized with zeros.

### Comments

Single-line comments start with `//`:
```javascript
// This is a comment
output "Hello, World!"
```

### Operators

#### Arithmetic Operators

| Operator | Description    | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Subtraction    | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| inc      | Increment      | inc x   |
| dec      | Decrement      | dec x   |
| ^        | Exponent       | x ^ y   |

#### Comparison Operators

| Operator | Description              | Example |
|----------|--------------------------|---------|
| ==       | Equal to                 | x == y  |
| !=       | Not equal to            | x != y  |
| >        | Greater than            | x > y   |
| >=       | Greater than or equal   | x >= y  |
| <        | Less than               | x < y   |
| <=       | Less than or equal      | x <= y  |

### Control Structures

#### If-Else Statements

```javascript
if condition {
    statement
} else {
    statement
}
```

Example:
```javascript
name = input "Enter your name: "
if name == "Ed Sheeran" {
    output "Hi, " + name
} else {
    output "Bye, " + name
}
```

#### While Loops

```javascript
while condition 
do {
    statement
}
```

Example:
```javascript
start = 1
end = 10
while start != end
do {
    output start
    inc start
}
```

### Data Structures

#### Lists/Arrays

Create and use arrays:
```javascript
// 1D Array example
numbers = array[5]
numbers[0] = 10
numbers[1] = 20
output numbers[0]     // Outputs: 10

// 2D Array example
matrix = array[2][2]
matrix[0][0] = 1
matrix[0][1] = 2
output matrix[0][1]   // Outputs: 2
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT
