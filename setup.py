#!/usr/bin/env python3
# Copyright (c) 2025 Ashutosh Sharma. All rights reserved.

from sys import argv
from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension
from setuptools.command.build_ext import build_ext
import subprocess
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

class CustomBuildExt(build_ext):
    def run(self):
        # Ensure directories exist
        for dir_path in [
            'src/bindings/rust/array_ops',
            'src/bindings/cpp',
            'src/bindings/go',
            'src/bindings/julia',
            'src/bindings/wasm'
        ]:
            ensure_dir(dir_path)
            
        # Build Rust components
        subprocess.check_call(['cargo', 'build', '--release'])
        
        # Build language-specific components
        try:
            # C++ components
            subprocess.check_call(['cmake', '.'], cwd='src/bindings/cpp')
            subprocess.check_call(['make'], cwd='src/bindings/cpp')
            
            # Go components
            subprocess.check_call(['go', 'build', '-buildmode=c-shared'], cwd='src/bindings/go')
            
            # Julia components
            subprocess.check_call(['julia', 'build.jl'], cwd='src/bindings/julia')
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to build some components: {e}")
            print("Continuing with partial build...")
        
        super().run()

setup(
    name='aslang',
    version='0.1.0',
    description='A high-performance multi-language programming language',
    long_description=open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/alexshcer/aslang", 
    project_urls={
        "Documentation": "https://github.com/alexshcer/aslang/tree/main/docs",
        "Issue tracker": "https://github.com/alexshcer/aslang/issues",
    },
    author='Ashutosh Sharma',
    author_email='ashutoshsharmawhy@gmail.com',
    license='MIT', 
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Rust',
        'Programming Language :: C++',
        'Programming Language :: Go',
        'Programming Language :: Julia',
    ],
    keywords='aslang, programming language, multi-language, hybrid', 
    packages=find_packages(),
    install_requires=[
        'sly>=0.4',
        'setuptools-rust>=1.5.2',
    ],
    python_requires='>=3.6',
    rust_extensions=[
        RustExtension(
            "aslang.core",
            "Cargo.toml",
            binding=Binding.PyO3
        ),
    ],
    zip_safe=False,
    cmdclass={
        'build_ext': CustomBuildExt,
    },
    include_package_data=True,
)