from distutils.core import setup
from distutils.extension import Extension
from distutils.sysconfig import get_python_lib
from Cython.Build import cythonize
import os, sys, inspect

numpy_inc = os.path.join(get_python_lib(plat_specific=1), 'numpy/core/include')
current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_path = os.path.dirname(current_path)
sys.path.insert(0, parent_path)

import config_path as cp

lognormal_mocks_include_path = parent_path + '/lognormal_mocks/include'
lognormal_mocks_lib_path = parent_path + '/build/lib'

lognormal_mocks_extension = Extension(name='py_lognormal_mocks',
                                      sources=['python/py_lognormal_mocks.pyx'],
                                      include_dirs = [numpy_inc, lognormal_mocks_include_path, cp.healpix_include_path, cp.lapack_include_path, cp.sharp_include_path],
                                      libraries=['lognormal_mocks', 'gsl','gslcblas', 'healpix','cfitsio','gomp', 'lapack','sharp', 'fftpack', 'c_utils', 'gfortran', 'mvec'],
                                      library_dirs = [lognormal_mocks_lib_path, cp.healpix_lib_path, cp.lapack_lib_path, cp.sharp_lib_path, cp.glibc_lib_path],
                                      extra_compile_args=['-fPIC','-Wall','-g']
)

setup(name='py_lognormal_mocks',
      ext_modules=cythonize([lognormal_mocks_extension]))
