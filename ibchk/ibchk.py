"""
RBMM - Iterative Block Cholesky decomposition
By Josh Brown
CS 3513 - Numerical methods
Due - 2/24/16
"""
from sys import argv
import math
import numpy

BASE_SIZE = int(argv[3])
NP = numpy

def cholesky_decompose(mat_in):
    """
    Use Cholesky's algorithm to decompose an nxn matrix and return L
    I used the algorithm found in this video.
    https://www.youtube.com/watch?v=NppyUqgQqd0
    """
    size = mat_in.shape[0]
    print "decomposing %dx%d matrix" % (size, size)
    matrix_l = NP.zeros([size, size])
    for i in xrange(size):
        for j in xrange(i + 1):
            line_sum = 0.0
            if i == j:
                for k in xrange(j):
                    line_sum += matrix_l[i, k] * matrix_l[i, k]
                matrix_l[i, i] = math.sqrt(mat_in[i, i] - line_sum)
            else:
                for k in xrange(j):
                    line_sum += matrix_l[j, k] * matrix_l[i, k]
                matrix_l[i, j] = (mat_in[i, j] - line_sum) / matrix_l[j, j]

    return matrix_l

def block_cholesky(mat_in, mat_l):
    """
    block decompose
    """
    for i in range(0, mat_in.shape[0], BASE_SIZE):
        mat_l[i:i + BASE_SIZE, i:i + BASE_SIZE] += \
            cholesky_decompose(mat_in[i:i + BASE_SIZE, i:i + BASE_SIZE])
        print mat_l


def main(file_a, out_file):
    """
    Takes a matrix from file A, calculates a Gram matrix by taking A transpose
    multipied by A. Then outputs the Cholesky decomposition L of that Gram
    matrix to the specified output file.
    """
    matrix_a = NP.matrix(NP.loadtxt(file_a))
    matrix_g = matrix_a.T * matrix_a
    matrix_l = NP.zeros([matrix_g.shape[0], matrix_g.shape[0]])
    block_cholesky(matrix_g, matrix_l)

    # print NP.savetxt(out_file, matrix_out, '%20.8f')


if __name__ == '__main__':
    main(argv[1], argv[2])
