use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use std::vec::Vec;

#[pyclass]
struct NDArray {
    data: Vec<f64>,
    dims: Vec<usize>,
    strides: Vec<usize>,
}

#[pymethods]
impl NDArray {
    #[new]
    fn new(dims: Vec<usize>) -> PyResult<Self> {
        if dims.is_empty() {
            return Err(PyValueError::new_err("Dimensions cannot be empty"));
        }
        
        let size: usize = dims.iter().product();
        let mut strides = vec![1; dims.len()];
        for i in (0..dims.len()-1).rev() {
            strides[i] = strides[i + 1] * dims[i + 1];
        }
        
        Ok(NDArray {
            data: vec![0.0; size],
            dims,
            strides,
        })
    }

    fn get(&self, indices: Vec<usize>) -> PyResult<f64> {
        if indices.len() != self.dims.len() {
            return Err(PyValueError::new_err("Wrong number of indices"));
        }
        
        for (idx, &dim) in indices.iter().zip(self.dims.iter()) {
            if idx >= dim {
                return Err(PyValueError::new_err(format!("Index {} out of bounds for dimension {}", idx, dim)));
            }
        }
        
        let flat_idx = indices.iter()
            .zip(self.strides.iter())
            .map(|(&idx, &stride)| idx * stride)
            .sum();
            
        Ok(self.data[flat_idx])
    }

    fn set(&mut self, indices: Vec<usize>, value: f64) -> PyResult<()> {
        if indices.len() != self.dims.len() {
            return Err(PyValueError::new_err("Wrong number of indices"));
        }
        
        for (idx, &dim) in indices.iter().zip(self.dims.iter()) {
            if idx >= dim {
                return Err(PyValueError::new_err(format!("Index {} out of bounds for dimension {}", idx, dim)));
            }
        }
        
        let flat_idx = indices.iter()
            .zip(self.strides.iter())
            .map(|(&idx, &stride)| idx * stride)
            .sum();
            
        self.data[flat_idx] = value;
        Ok(())
    }

    fn shape(&self) -> Vec<usize> {
        self.dims.clone()
    }
}

#[pymodule]
fn array_ops(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<NDArray>()?;
    Ok(())
} 