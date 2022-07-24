import setuptools
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["hello.pyx", "compute.pyx"], build_dir="build"),
                                           script_args=['build'], 
                                           options={'build':{'build_lib':'.'}})
