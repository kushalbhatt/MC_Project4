from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_module = Extension("openmpext",["testCython.pyx"], extra_compile_args=['-fopenmp'],extra_link_arts=['fopenmp'],)
setup(name='OpenMP app', cmdclass={'build_ext':build_ext}, ext_modules=[ext_module],)

#Which will leave a file in your local directory called helloworld.so in unix or helloworld.pyd in Windows.
#Now to use this file: start the python interpreter and simply import it as if it was a regular python module:
#import name_of_*.pyx
