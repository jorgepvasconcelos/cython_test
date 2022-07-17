import setuptools
import Cython.Build as cb

setuptools.setup(name='My Cython Project',     ext_modules=cb.cythonize('list_sum_pyx.pyx'))