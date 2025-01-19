# author: ashuwhy

from sys import argv
from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension
from setuptools.command.build_ext import build_ext
import subprocess


if len(argv) > 1 and argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
  pass #will add file assoc soon  

 
classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

class CustomBuildExt(build_ext):
    def run(self):
        # Build Rust components
        subprocess.check_call(['cargo', 'build', '--release'], cwd='aslang/array_ops')
        subprocess.check_call(['cargo', 'build', '--release'], cwd='aslang/wasm_ops')
        
        # Build C++ components
        subprocess.check_call(['cmake', '.'], cwd='aslang/cpp_ops')
        subprocess.check_call(['make'], cwd='aslang/cpp_ops')
        
        # Build Go components
        subprocess.check_call(['go', 'build', '-buildmode=c-shared'], cwd='aslang/go_ops')
        
        # Build Julia components
        subprocess.check_call(['julia', 'build.jl'], cwd='aslang/julia_ops')
        
        super().run()

setup(
  name='as',
  version='0.1',
  description='A Progamming Language.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/alexshcer/aslang", 
  project_urls={
   "Documentation": "https://github.com/alexshcer/aslang/tree/main#getting-started",
   "Issue tracker": "https://github.com/alexshcer/aslang/issues",
   },
  author='asadev',
  author_email='alexmerser591@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='as,language,as lang', 
  packages=find_packages(),
  install_requires= ['sly'],
  python_requires='>=3.6',
  rust_extensions=[
    RustExtension(
      "aslang.array_ops",
      "aslang/array_ops/Cargo.toml",
      binding=Binding.PyO3
    ),
    RustExtension(
      "aslang.wasm_ops",
      "aslang/wasm_ops/Cargo.toml",
      binding=Binding.PyO3
    )
  ],
  zip_safe=False,
  cmdclass={
    'build_ext': CustomBuildExt,
  },
)