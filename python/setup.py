from distutils.core import setup
from distutils.extension import Extension
from distutils.sysconfig import get_python_lib
from Cython.Build import cythonize
import os, sys, inspect

numpy_inc = os.path.join(get_python_lib(plat_specific=1), 'numpy/core/include')
current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_path = os.path.dirname(current_path)

# dependence paths from input
healpix_path = input("Enter healpix path:")
lapack_path = input("Enter lapack path:")
sharp_path = input("Enter libsharp path:")

# include paths
healpix_include_path = healpix_path + '/include'
lapack_include_path = lapack_path
sharp_include_path = sharp_path + '/auto/include'
lognormal_mocks_include_path = parent_path + '/lognormal_mocks/include'

# library paths
libhealpix_path = healpix_path + '/lib'
liblapack_path = lapack_path
libsharp_path = sharp_path + '/auto/lib'
libmvec_path = '/lib/x86_64-linux-gnu'
liblognormal_mocks_path = parent_path + '/build/lib'

lognormal_mocks_extension = Extension(name='py_lognormal_mocks',
                                      sources=['python/py_lognormal_mocks.pyx'],
                                      include_dirs = [numpy_inc, lognormal_mocks_include_path, healpix_include_path, lapack_include_path, sharp_include_path],
                                      libraries=['lognormal_mocks', 'gsl','gslcblas', 'healpix','cfitsio','gomp', 'lapack','sharp', 'fftpack', 'c_utils', 'gfortran', 'mvec'],
                                      library_dirs = [liblognormal_mocks_path, libhealpix_path, liblapack_path, libsharp_path, libmvec_path],
                                      extra_compile_args=['-fPIC','-Wall','-g']
)

setup(author='Hongbo Cai',
      author_email='hoc34@pitt.edu',
      name='py_lognormal_mocks',
      ext_modules=cythonize([lognormal_mocks_extension]))
