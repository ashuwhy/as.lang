// Copyright (c) 2025 Ashutosh Sharma. All rights reserved.

#[derive(Debug)]
pub enum Expression {
    Number(f64),
    String(String),
    Identifier(String),
    Call {
        function: String,
        arguments: Vec<Expression>,
    },
    Array {
        elements: Vec<Expression>,
    },
}

#[derive(Debug)]
pub enum Statement {
    Let {
        name: String,
        value: Expression,
    },
    Output(Expression),
    Function {
        name: String,
        params: Vec<String>,
        body: Vec<Statement>,
    },
}

#[derive(Debug)]
pub struct AST {
    pub statements: Vec<Statement>,
}

pub struct Parser {
    tokens: Vec<String>,
    current: usize,
}

impl Parser {
    pub fn new() -> Self {
        Parser {
            tokens: Vec::new(),
            current: 0,
        }
    }

    pub fn parse(&mut self, input: &str) -> Result<AST, String> {
        self.tokenize(input);
        let mut statements = Vec::new();
        
        while !self.is_at_end() {
            statements.push(self.parse_statement()?);
        }
        
        Ok(AST { statements })
    }

    fn tokenize(&mut self, input: &str) {
        self.tokens = input
            .split_whitespace()
            .map(|s| s.to_string())
            .collect();
        self.current = 0;
    }

    fn parse_statement(&mut self) -> Result<Statement, String> {
        match self.peek().as_str() {
            "let" => self.parse_let(),
            "output" => self.parse_output(),
            "fn" => self.parse_function(),
            _ => Err("Unexpected token".to_string()),
        }
    }

    fn parse_let(&mut self) -> Result<Statement, String> {
        self.advance(); // consume 'let'
        let name = self.advance();
        
        if self.advance() != "=" {
            return Err("Expected '=' after variable name".to_string());
        }
        
        let value = self.parse_expression()?;
        
        Ok(Statement::Let { name, value })
    }

    fn parse_output(&mut self) -> Result<Statement, String> {
        self.advance(); // consume 'output'
        let expr = self.parse_expression()?;
        Ok(Statement::Output(expr))
    }

    fn parse_function(&mut self) -> Result<Statement, String> {
        self.advance(); // consume 'fn'
        let name = self.advance();
        
        if self.advance() != "(" {
            return Err("Expected '(' after function name".to_string());
        }
        
        let mut params = Vec::new();
        while self.peek() != ")" {
            params.push(self.advance());
            if self.peek() == "," {
                self.advance();
            }
        }
        self.advance(); // consume ')'
        
        if self.advance() != "{" {
            return Err("Expected '{' after function parameters".to_string());
        }
        
        let mut body = Vec::new();
        while self.peek() != "}" {
            body.push(self.parse_statement()?);
        }
        self.advance(); // consume '}'
        
        Ok(Statement::Function { name, params, body })
    }

    fn parse_expression(&mut self) -> Result<Expression, String> {
        let token = self.peek();
        
        if let Ok(num) = token.parse::<f64>() {
            self.advance();
            Ok(Expression::Number(num))
        } else if token.starts_with("\"") {
            self.advance();
            Ok(Expression::String(token.trim_matches('"').to_string()))
        } else if self.peek_next() == "(" {
            self.parse_call()
        } else if token == "[" {
            self.parse_array()
        } else {
            self.advance();
            Ok(Expression::Identifier(token))
        }
    }

    fn parse_call(&mut self) -> Result<Expression, String> {
        let function = self.advance();
        self.advance(); // consume '('
        
        let mut arguments = Vec::new();
        while self.peek() != ")" {
            arguments.push(self.parse_expression()?);
            if self.peek() == "," {
                self.advance();
            }
        }
        self.advance(); // consume ')'
        
        Ok(Expression::Call { function, arguments })
    }

    fn parse_array(&mut self) -> Result<Expression, String> {
        self.advance(); // consume '['
        
        let mut elements = Vec::new();
        while self.peek() != "]" {
            elements.push(self.parse_expression()?);
            if self.peek() == "," {
                self.advance();
            }
        }
        self.advance(); // consume ']'
        
        Ok(Expression::Array { elements })
    }

    fn advance(&mut self) -> String {
        let token = self.tokens[self.current].clone();
        self.current += 1;
        token
    }

    fn peek(&self) -> String {
        if self.is_at_end() {
            String::new()
        } else {
            self.tokens[self.current].clone()
        }
    }

    fn peek_next(&self) -> String {
        if self.current + 1 >= self.tokens.len() {
            String::new()
        } else {
            self.tokens[self.current + 1].clone()
        }
    }

    fn is_at_end(&self) -> bool {
        self.current >= self.tokens.len()
    }
} 