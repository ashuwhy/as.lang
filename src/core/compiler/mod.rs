// Copyright (c) 2025 Ashutosh Sharma. All rights reserved.

use crate::parser::{AST, Expression, Statement};
use std::collections::HashMap;

#[derive(Debug)]
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

pub struct Compiler {
    bytecode: Vec<Opcode>,
    variables: HashMap<String, usize>,
    functions: HashMap<String, usize>,
}

impl Compiler {
    pub fn new() -> Self {
        Compiler {
            bytecode: Vec::new(),
            variables: HashMap::new(),
            functions: HashMap::new(),
        }
    }

    pub fn compile(&mut self, ast: &AST) -> Result<Vec<u8>, String> {
        self.bytecode.clear();
        
        for statement in &ast.statements {
            self.compile_statement(statement)?;
        }
        
        // Serialize bytecode to bytes
        let mut bytes = Vec::new();
        for opcode in &self.bytecode {
            self.serialize_opcode(opcode, &mut bytes);
        }
        
        Ok(bytes)
    }

    fn compile_statement(&mut self, statement: &Statement) -> Result<(), String> {
        match statement {
            Statement::Let { name, value } => {
                self.compile_expression(value)?;
                self.bytecode.push(Opcode::StoreVar(name.clone()));
                self.variables.insert(name.clone(), self.variables.len());
            }
            Statement::Output(expr) => {
                self.compile_expression(expr)?;
                self.bytecode.push(Opcode::Output);
            }
            Statement::Function { name, params, body } => {
                let start_pos = self.bytecode.len();
                self.functions.insert(name.clone(), start_pos);
                
                // Add parameters to variables
                for param in params {
                    self.variables.insert(param.clone(), self.variables.len());
                }
                
                // Compile function body
                for stmt in body {
                    self.compile_statement(stmt)?;
                }
                
                self.bytecode.push(Opcode::Return);
            }
        }
        Ok(())
    }

    fn compile_expression(&mut self, expr: &Expression) -> Result<(), String> {
        match expr {
            Expression::Number(n) => {
                self.bytecode.push(Opcode::LoadConst(*n));
            }
            Expression::String(s) => {
                self.bytecode.push(Opcode::LoadString(s.clone()));
            }
            Expression::Identifier(name) => {
                if !self.variables.contains_key(name) {
                    return Err(format!("Undefined variable: {}", name));
                }
                self.bytecode.push(Opcode::LoadVar(name.clone()));
            }
            Expression::Call { function, arguments } => {
                // Compile arguments
                for arg in arguments {
                    self.compile_expression(arg)?;
                }
                
                if !self.functions.contains_key(function) {
                    return Err(format!("Undefined function: {}", function));
                }
                
                self.bytecode.push(Opcode::Call(function.clone(), arguments.len()));
            }
            Expression::Array { elements } => {
                // Compile array elements
                for element in elements {
                    self.compile_expression(element)?;
                }
                
                self.bytecode.push(Opcode::MakeArray(elements.len()));
            }
        }
        Ok(())
    }

    fn serialize_opcode(&self, opcode: &Opcode, bytes: &mut Vec<u8>) {
        match opcode {
            Opcode::LoadConst(n) => {
                bytes.push(1);
                bytes.extend(&n.to_le_bytes());
            }
            Opcode::LoadString(s) => {
                bytes.push(2);
                bytes.extend(&(s.len() as u32).to_le_bytes());
                bytes.extend(s.as_bytes());
            }
            Opcode::LoadVar(name) => {
                bytes.push(3);
                bytes.extend(&(*self.variables.get(name).unwrap() as u32).to_le_bytes());
            }
            Opcode::StoreVar(name) => {
                bytes.push(4);
                bytes.extend(&(*self.variables.get(name).unwrap() as u32).to_le_bytes());
            }
            Opcode::Call(name, argc) => {
                bytes.push(5);
                bytes.extend(&(*self.functions.get(name).unwrap() as u32).to_le_bytes());
                bytes.extend(&(*argc as u32).to_le_bytes());
            }
            Opcode::MakeArray(size) => {
                bytes.push(6);
                bytes.extend(&(*size as u32).to_le_bytes());
            }
            Opcode::Return => {
                bytes.push(7);
            }
            Opcode::Output => {
                bytes.push(8);
            }
        }
    }
} 