from distutils.core import setup
from distutils.extension import Extension
from distutils.sysconfig import get_python_lib
from Cython.Build import cythonize
import os

numpy_inc = os.path.join(get_python_lib(plat_specific=1), 'numpy/core/include')

# include paths
healpix_include_path = '/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82/include'
lapack_include_path = '/home/ketchup/tools/lapack-3.11.0'
sharp_include_path = '/home/ketchup/tools/libsharp/auto/include'
lognormal_mocks_include_path = '/home/ketchup/tools/lognormal_mocks/lognormal_mocks/include'

# lib paths
liblognormal_mocks_path = '/home/ketchup/tools/lognormal_mocks/build/lib'
libhealpix_path = '/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82/lib'
liblapack_path = '/home/ketchup/tools/lapack-3.11.0'
libsharp_path = '/home/ketchup/tools/libsharp/auto/lib'
libmvec_path = '/lib/x86_64-linux-gnu'

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
