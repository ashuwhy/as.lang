use wasm_bindgen::prelude::*;
use serde::{Serialize, Deserialize};

#[wasm_bindgen]
pub struct Runtime {
    variables: Vec<JsValue>,
}

#[wasm_bindgen]
impl Runtime {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Runtime {
        Runtime {
            variables: Vec::new(),
        }
    }

    pub fn execute(&mut self, code: &str) -> Result<JsValue, JsValue> {
        // Basic execution for now
        Ok(JsValue::from_str(&format!("Executed: {}", code)))
    }

    pub fn get_variable(&self, index: usize) -> Option<JsValue> {
        self.variables.get(index).cloned()
    }

    pub fn set_variable(&mut self, index: usize, value: JsValue) {
        if index >= self.variables.len() {
            self.variables.resize_with(index + 1, || JsValue::NULL);
        }
        self.variables[index] = value;
    }
}

#[derive(Serialize, Deserialize)]
struct CompilationResult {
    bytecode: Vec<u8>,
    metadata: String,
}

#[wasm_bindgen]
pub fn compile(source: &str) -> Result<JsValue, JsValue> {
    let result = CompilationResult {
        bytecode: source.as_bytes().to_vec(),
        metadata: "Compiled with WASM".to_string(),
    };
    
    Ok(serde_json::to_string(&result)
        .map_err(|e| JsValue::from_str(&e.to_string()))?
        .into())
} 