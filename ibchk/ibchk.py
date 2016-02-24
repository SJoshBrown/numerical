"""
RBMM - Iterative Block Cholesky decomposition
By Josh Brown
CS 3513 - Numerical methods
Due - 2/24/16
"""
from sys import argv
import math
import numpy

NP = numpy


def cholesky_decompose(to_decompose, mat_l):
    """
    Use Cholesky's algorithm to decompose an nxn matrix to_decompose and add it
    to a predefined zero matrix mat_l I developed the algorithm using the method
    found in this video.
    https://www.youtube.com/watch?v=NppyUqgQqd0
    """
    size = to_decompose.shape[0]
    for i in xrange(size):
        for j in xrange(i + 1):
            line_sum = 0.0
            if i == j:
                for k in xrange(j):
                    line_sum += mat_l[i, k] * mat_l[i, k]
                mat_l[i, i] = math.sqrt(to_decompose[i, i] - line_sum)
            else:
                for k in xrange(j):
                    line_sum += mat_l[j, k] * mat_l[i, k]
                mat_l[i, j] = (to_decompose[i, j] - line_sum) / mat_l[j, j]


def block_cholesky(mat_in, mat_l, block_size):
    """
    Takes two arguments mat_in and mat_l. Decomposes matrix_in into
    pre-initialized zero matrix matrix_l using blocks of size block_size.
    """
    for i in range(0, mat_in.shape[0], block_size):
        g00 = mat_in[i:i + block_size, i:i + block_size]
        l00 = mat_l[i:i + block_size, i:i + block_size]
        cholesky_decompose(g00, l00)
        g10 = mat_in[i + block_size:, i:i + block_size]
        l10 = mat_l[i + block_size:, i:i + block_size]
        forwardsub(l10, l00, g10)

        mat_in[i + block_size:, i + block_size:] -=\
            NP.matrix(l10) * NP.matrix(l10.T)


def forwardsub(l10, l00, g10):
    """
    Use lower triangular matrix l00 to calulate l10 from g10 using forward
    substitution.
    """
    g10_trans = NP.matrix(g10.T)
    l10_trans = NP.matrix(l10.T)
    for i in range(0, l10_trans.shape[1]):
        for j in range(0, l00.shape[1]):
            row_sum = 0
            for k in xrange(j + 1):
                if j == k:
                    l10_trans[k, i] += (g10_trans[j, i] - row_sum) / l00[j, j]
                else:
                    row_sum += l00[j, k] * l10_trans[k, i]

    l10 += NP.matrix(l10_trans.T)


def is_pos_def(matrix_in):
    """
    Returns true if the matrix is a positive definite matrix. I found the
    algorithm at https://stackoverflow.com/questions/16266720/
    """
    return NP.all(NP.linalg.eigvals(matrix_in) > 0)


def main(file_a, out_file, base_size):
    """
    Takes a matrix from file A, calculates a Gram matrix by taking A transpose
    multipied by A. Then outputs the Cholesky decomposition L of that Gram
    matrix to the specified output file.
    """
    matrix_a = NP.matrix(NP.loadtxt(file_a))
    matrix_g = matrix_a.T * matrix_a
    matrix_l = NP.zeros([matrix_g.shape[0], matrix_g.shape[0]])
    if is_pos_def(matrix_g):
        block_cholesky(matrix_g, matrix_l, base_size)
        NP.savetxt(out_file, matrix_l, '%15.8f')
    else:
        print "Error, the input matrix is not positive definite."


if __name__ == '__main__':
    try:
        int(argv[3])
        BASE_SIZE = int(argv[3])
    except (ValueError, IndexError):
        BASE_SIZE = 8
    main(argv[1], argv[2], BASE_SIZE)
