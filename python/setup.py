from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import subprocess as sbp
import os.path as osp

lognormal_mocks_extension = Extension(name='py_lognormal_mocks',
                                      sources=['python/py_lognormal_mocks.pyx'],
                                      libraries=['lognormal_mocks', 'gsl','gslcblas','healpix','cfitsio','gomp','lapack', 'gfortran', 'sharp', 'fftpack', 'gcc'],                                library_dirs=['/home/ketchup/tools/lognormal_mocks/build/lib','/home/ketchup/gsl/lib', '/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82/lib', '/home/ketchup/tools/lapack-3.11.0'],
                                      include_dirs = [numpy.get_include(),'lognormal_mocks/include/', '/home/ketchup/gsl/include/gsl', '/home/ketchup/tools/Healpix_3.82_2022Jul28/Healpix_3.82', '/home/ketchup/tools/lapack-3.11.0/LAPACKE/include'])

setup(name='py_lognormal_mocks',
      ext_modules=cythonize([lognormal_mocks_extension]))

# setup(author='Hongbo Cai',
#       author_email='hoc34@pitt.edu',
#       name='pytoy',
#       ext_modules=cythonize([toy_extension]))
