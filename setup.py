# author: ashuwhy

from sys import argv
from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension


if len(argv) > 1 and argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
  pass #will add file assoc soon  

 
classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

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
    )
  ],
  zip_safe=False
)