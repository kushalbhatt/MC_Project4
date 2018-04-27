from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_module = Extension("openmpext",["task1_6pythonDTW.pyx"], extra_compile_args=['-fopenmp'],extra_link_arts=['fopenmp'],)
setup(name='OpenMP app', cmdclass={'build_ext':build_ext}, ext_modules=[ext_module],)
