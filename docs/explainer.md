# AS Lang - A Multi-Language Programming System

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Core Components](#core-components)
5. [Language Bindings](#language-bindings)
6. [Build System](#build-system)
7. [Installation Process](#installation-process)
8. [Code Walkthrough](#code-walkthrough)
9. [Examples](#examples)

## Overview

AS Lang is a high-performance multi-language programming system that combines the strengths of multiple programming languages:
- Rust for core language implementation and memory safety
- C++ for SIMD operations and low-level performance
- Go for concurrent operations
- Julia for scientific computing
- WebAssembly for browser support
- Python for high-level bindings

## Prerequisites

To understand and work with this project, you should have knowledge of:

1. Programming Languages:
   - Rust (intermediate level)
   - C++ (basic level)
   - Python (intermediate level)
   - Go (basic level)
   - Julia (basic level)

2. Concepts:
   - Compiler design
   - Virtual machines
   - SIMD operations
   - Concurrent programming
   - FFI (Foreign Function Interface)
   - WebAssembly

3. Tools:
   - Cargo (Rust package manager)
   - CMake
   - Python setuptools
   - Git

## Project Structure

```
.
├── src/
│   ├── core/           # Core language implementation
│   │   ├── compiler/   # Compiler implementation
│   │   ├── parser/     # Parser implementation
│   │   └── lib.rs      # Core library exports
│   ├── runtime/        # Runtime engine
│   └── bindings/       # Language-specific bindings
│       ├── rust/       # Rust array operations
│       ├── cpp/        # C++ SIMD operations
│       ├── go/         # Go concurrent operations
│       ├── julia/      # Julia scientific computing
│       └── wasm/       # WebAssembly interface
├── docs/              # Documentation
├── lib/               # Shared libraries
└── tests/             # Test suites
```

## Core Components

### 1. Parser (`src/core/parser/mod.rs`)

The parser is responsible for converting source code into an Abstract Syntax Tree (AST).

```rust
pub enum Expression {
    Number(f64),
    String(String),
    Identifier(String),
    Call { function: String, arguments: Vec<Expression> },
    Array { elements: Vec<Expression> },
}

pub enum Statement {
    Let { name: String, value: Expression },
    Output(Expression),
    Function { name: String, params: Vec<String>, body: Vec<Statement> },
}
```

Key components:
- `Expression`: Represents values and operations
- `Statement`: Represents program structure
- `Parser`: Converts text into AST
- `tokenize()`: Splits input into tokens
- `parse_statement()`: Parses individual statements
- `parse_expression()`: Parses expressions

### 2. Compiler (`src/core/compiler/mod.rs`)

The compiler converts AST into bytecode.

```rust
pub enum Opcode {
    LoadConst(f64),
    LoadString(String),
    LoadVar(String),
    StoreVar(String),
    Call(String, usize),
    MakeArray(usize),
    Return,
    Output,
}
```

Key features:
- Stack-based bytecode
- Variable management
- Function calls
- Array operations

### 3. Runtime (`src/runtime/mod.rs`)

The runtime executes bytecode.

```rust
enum Value {
    Number(f64),
    String(String),
    Array(Vec<Value>),
    None,
}
```

Features:
- Stack-based execution
- Variable storage
- Function management
- Output handling

## Language Bindings

### 1. Rust Array Operations (`src/bindings/rust/array_ops/`)

Provides high-performance array operations:

```rust
#[pyclass]
struct NDArray {
    data: Vec<f64>,
    dims: Vec<usize>,
    strides: Vec<usize>,
}
```

Features:
- Multi-dimensional arrays
- Parallel processing
- Matrix operations
- Python integration via PyO3

### 2. C++ SIMD Operations (`src/bindings/cpp/`)

Implements SIMD-accelerated vector operations:

```cpp
void vector_add_f64(const double* a, const double* b, double* result, size_t size);
void vector_multiply_f64(const double* a, const double* b, double* result, size_t size);
void vector_scale_f64(const double* input, double scale, double* result, size_t size);
```

Features:
- AVX instructions
- Vectorized operations
- Fallback for non-SIMD cases

### 3. WebAssembly Support (`src/bindings/wasm/`)

Provides browser integration:

```rust
#[wasm_bindgen]
pub struct Runtime {
    variables: Vec<JsValue>,
}
```

Features:
- JavaScript interop
- Browser execution
- Variable management

## Build System

### 1. Cargo Configuration (`Cargo.toml`)

```toml
[workspace]
members = [
    ".",
    "src/bindings/rust/array_ops",
    "src/bindings/wasm"
]

[workspace.dependencies]
# Shared dependencies
```

### 2. CMake Configuration (`src/bindings/cpp/CMakeLists.txt`)

```cmake
# C++ build configuration
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```

### 3. Python Setup (`setup.py`)

```python
# Python package configuration and build process
```

## Installation Process

### Unix Systems (`install.sh`)

1. Dependency checks
2. Tool installation
3. Build process
4. Package installation

### Windows Systems (`install.bat`)

Similar process with Windows-specific commands.

## Code Examples

### Basic Usage

```python
# Hello World
output "Hello, World!"

# Variables
let message = "Welcome to AS Lang!"
output message

# Functions
fn greet(name) {
    output "Hello, " + name + "!"
}
```

### Array Operations

```python
# Create array
let arr = [1, 2, 3, 4]

# SIMD operations
let result = parallel_map(arr, 2.0)  # [2, 4, 6, 8]
```

## Performance Considerations

1. SIMD Acceleration
   - AVX instructions for vector operations
   - 4-wide double-precision operations

2. Parallel Processing
   - Rust's rayon for parallel iterators
   - Go's goroutines for concurrency

3. Memory Management
   - Rust's ownership system
   - Efficient array layouts
   - SIMD-friendly data alignment

## Future Development

1. Planned Features
   - JIT compilation
   - More SIMD operations
   - Enhanced type system
   - Module system

2. Optimization Opportunities
   - Better SIMD utilization
   - More parallel operations
   - Improved memory layout

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - Copyright (c) 2025 Ashutosh Sharma. All rights reserved. 