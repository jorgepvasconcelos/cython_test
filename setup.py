from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='list sum',
    ext_modules=cythonize("list_sum_pyx.pyx"),
    zip_safe=False
)
