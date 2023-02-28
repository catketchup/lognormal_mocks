from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import subprocess as sbp
import os.path as osp


lognormal_mocks_extension = Extension(name='lognormal_mocks',
                                      sources=['python/py_lognormal_mocks.pyx'],
                                      libraries=['lognormal_mocks'],
                                      library_dirs=['build/lib'],
                                      include_dirs=['lognormal_mocks/include',
                                                    numpy.get_include()])

# setup(author='Hongbo Cai',
#       author_email='hoc34@pitt.edu',
#       name='pytoy',
#       ext_modules=cythonize([toy_extension]))

setup(name='py_lognormal_mocks',
      ext_modules=cythonize([lognormal_mocks_extension]))
