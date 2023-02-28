MDIR := $(shell pwd)
IDIR = $(MDIR)/lognormal_mocks/include
SRCDIR = $(MDIR)/lognormal_mocks/src
LOCALDIR :=$(shell python -m site --user-site)

BLDDIR = $(MDIR)/build
LIBDIR = $(BLDDIR)/lib
PYDIR = $(MDIR)/python

$(shell if [ ! -e $(BLDDIR) ];then mkdir $(BLDDIR); mkdir $(LIBDIR); fi)

# CC = gcc

default: $(PYDIR)/py_lognormal_mocks.c

SYMMETRIC_LEGENDRE.H=$(IDIR)/symmetric_legendre.h
LOGNORMAL_MOCKS.H=$(IDIR)/lognormal_mocks.h

LOGNORMAL_MOCKS_STATS.C=$(SRCDIR)/lognormal_mocks_stats.c

LOGNORMAL_MOCKS_STATS.O=$(BLDDIR)/lognormal_mocks_stats.o


# gcc -c lognormal_mocks/src/lognormal_mocks_stats.c -o build/lognormal_mocks_stats.o -I lognormal_mocks/include -I /home/ketchup/gsl/include -lm
# ar rcs build/lib/liblognormal_mocks.a build/lognormal_mocks_stats.o

gcc -c $(LOGNORMAL_MOCKS_STATS.C) -o $(LOGNORMAL_MOCKS_STATS.O) -I $(IDIR) -lm
ar rcs $(LIBDIR)/liblognormal_mocks.a $(LOGNORMAL_MOCKS_STATS.O)

# python python/setup.py build_ext --inplace
# python python/setup.py install --user
python $(PYDIR)/setup.py build_ext --inplace
python $(PYDIR)/setup.py install --user

.PHONY: clean

clean:
	rm $(LOCALDIR)/lognormal*
