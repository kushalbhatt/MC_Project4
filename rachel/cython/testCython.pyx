#Rachel Dedinsky
#CSE 535 Project 4: Task 1.6
from cython.parallel cimport parallel,prange
from libc.stdlib cimport abort,malloc,free
cimport openmp

def testpar(int n):
	cdef int i,numthreads,total
	cdef int * squared
	cdef int * tripled
	cdef size_t size = 10
	with nogil,parallel(num_threads=2):
		numthreads = openmp.omp_get_num_threads()
		squared = <int *> malloc(sizeof(int) * n)
		tripled = <int *> malloc(sizeof(int) * n)
	for i in prange(n,schedule='dynamic'):
			sqaured[i] = i*i
			tripled[i] = i*i*i + squared[i]
	free(squared)
	free(tripled)
