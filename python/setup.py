from distutils.core import setup
from distutils.extension import Extension
from distutils.sysconfig import get_python_lib
from Cython.Build import cythonize
import numpy
import os
import subprocess as sbp
import os.path as osp

numpy_inc = os.path.join(get_python_lib(plat_specific=1), 'numpy/core/include')

lognormal_mocks_extension = Extension(name='py_lognormal_mocks',
                                      sources=['python/py_lognormal_mocks.pyx'],
                                      include_dirs = [numpy_inc,'/home/ketchup/tools/lognormal_mocks/lognormal_mocks/include', '/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82/include','/home/ketchup/tools/lapack-3.11.0','/home/ketchup/tools/libsharp/auto/include'],
                                    libraries=['/home/ketchup/tools/lognormal_mocks/build/lib/lognormal_mocks', 'gsl','gslcblas','/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82/lib/healpix','cfitsio','gomp','/home/ketchup/tools/lapack-3.11.0/lapack','/home/ketchup/tools/libsharp/auto/lib/sharp', '/home/ketchup/tools/libsharp/auto/lib/fftpack', '/home/ketchup/tools/libsharp/auto/lib/c_utils', 'gfortran', 'gcc', '/lib/x86_64-linux-gnu/mvec'])

setup(name='py_lognormal_mocks',
      ext_modules=cythonize([lognormal_mocks_extension]))

# setup(author='Hongbo Cai',
#       author_email='hoc34@pitt.edu',
#       name='pytoy',
#       ext_modules=cythonize([toy_extension]))
