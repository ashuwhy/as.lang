use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct WasmRuntime {
    memory: Vec<f64>,
}

#[wasm_bindgen]
impl WasmRuntime {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Self {
        WasmRuntime {
            memory: Vec::new(),
        }
    }
    
    pub fn create_array(&mut self, size: usize) -> usize {
        self.memory.resize(self.memory.len() + size, 0.0);
        self.memory.len() - size
    }
    
    pub fn set_value(&mut self, index: usize, value: f64) {
        if index < self.memory.len() {
            self.memory[index] = value;
        }
    }
    
    pub fn get_value(&self, index: usize) -> f64 {
        if index < self.memory.len() {
            self.memory[index]
        } else {
            0.0
        }
    }
} 