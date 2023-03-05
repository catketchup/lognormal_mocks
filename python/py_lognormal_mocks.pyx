import numpy as np
cimport numpy as np
from libc.stdlib cimport *
from libc.stdio cimport *
from libc.string cimport *
import cython
cimport cython
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free


cdef extern from "lognormal_mocks.h":
    void lognormal_mocks_stats_fullsky(
        int Nmaps, double *rhobar,
        int Nl, double *Cldelta,
        double *gaussbar, double *Clgauss,
        double *xidelta, int Nth
    )

# rhobar, Cldelta, gaussbar, Clgauss, xidelta are double *

def lognormal_mocks_stats(double[:] rhobar, double[:,:,::1] Cl, Ntheta):
    Nmaps = rhobar.size
    Nl = Cl.shape[2]

    cdef np.ndarray[np.float64_t, ndim=1] gaussbar = np.zeros(Nmaps) # output
    cdef np.ndarray[np.float64_t, ndim=3] Clgauss = np.zeros([Nmaps, Nmaps, Nl]) # output
    cdef np.ndarray[np.float64_t, ndim=3] xidelta = np.zeros([Nmaps, Nmaps, Ntheta]) # input

    lognormal_mocks_stats_fullsky(Nmaps, &rhobar[0], Nl, &Cl[0,0,0], &gaussbar[0], &Clgauss[0,0,0], &xidelta[0,0,0], Ntheta)

    return (gaussbar, Clgauss)
