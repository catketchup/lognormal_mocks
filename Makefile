MDIR := $(shell pwd)
IDIR = $(MDIR)/lognormal_mocks/include
SRCDIR = $(MDIR)/lognormal_mocks/src
LOCALDIR :=$(shell python -m site --user-site)

BLDDIR = $(MDIR)/build
LIBDIR = $(BLDDIR)/lib
PYDIR = $(MDIR)/python

$(shell if [ ! -e $(BLDDIR) ];then mkdir $(BLDDIR); mkdir $(LIBDIR); fi)

default: py_lognormal_mocks

build/healpix_legendre_c.o: lognormal_mocks/src/healpix_legendre_c.c
	gcc -c lognormal_mocks/src/healpix_legendre_c.c -o build/healpix_legendre_c.o -I 	lognormal_mocks/include -I -lm -fPIC -Wall -g

build/symmetric_legendre.o: lognormal_mocks/src/symmetric_legendre.c
	gcc -c lognormal_mocks/src/symmetric_legendre.c -o build/symmetric_legendre.o -I lognormal_mocks/include -I -lm -fPIC -Wall -g

build/lognormal_mocks_stats.o: lognormal_mocks/src/lognormal_mocks_stats.c
	gcc -c lognormal_mocks/src/lognormal_mocks_stats.c -o build/lognormal_mocks_stats.o -I lognormal_mocks/include -I -lm -fPIC -Wall -g

build/lib/liblognormal_mocks.a: build/lognormal_mocks_stats.o build/healpix_legendre_c.o build/symmetric_legendre.o
	ar rcs build/lib/liblognormal_mocks.a build/lognormal_mocks_stats.o build/healpix_legendre_c.o build/symmetric_legendre.o

py_lognormal_mocks: $(PYDIR)/setup.py $(PYDIR)/py_lognormal_mocks.pyx build/lib/liblognormal_mocks.a
	python python/setup.py build_ext --inplace
	python python/setup.py install --user

.PHONY: clean

clean:
	rm -rf $(BLDDIR)
	rm -rf $(LIBDIR)
	rm $(MDIR)/*.so
	rm $(LOCALDIR)/py_lognormal*
	rm $(PYDIR)/*.c

# CC = gcc
