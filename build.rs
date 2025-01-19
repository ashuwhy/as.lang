use std::env;
use std::path::PathBuf;

fn main() {
    // Get output directory
    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());

    // Build C++ components
    let cpp_build = cmake::build("src/bindings/cpp");
    println!("cargo:rustc-link-search=native={}", cpp_build.display());
    println!("cargo:rustc-link-lib=dylib=aslang_cpp_ops");

    // Link Go library
    println!("cargo:rustc-link-search=native=src/bindings/go");
    println!("cargo:rustc-link-lib=dylib=go_ops");

    // Link Julia library
    println!("cargo:rustc-link-search=native=src/bindings/julia");
    println!("cargo:rustc-link-lib=dylib=julia_ops");

    // Generate bindings
    let bindings = bindgen::Builder::default()
        .header("src/bindings/cpp/include/simd_ops.h")
        .generate()
        .expect("Unable to generate bindings");

    bindings
        .write_to_file(out_dir.join("bindings.rs"))
        .expect("Couldn't write bindings!");

    // Rebuild if these files change
    println!("cargo:rerun-if-changed=src/bindings/cpp/src/simd_ops.cpp");
    println!("cargo:rerun-if-changed=src/bindings/cpp/include/simd_ops.h");
    println!("cargo:rerun-if-changed=src/bindings/go/libgo_ops.so");
    println!("cargo:rerun-if-changed=src/bindings/julia/libjulia_ops.so");
} 