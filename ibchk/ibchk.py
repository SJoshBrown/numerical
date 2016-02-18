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
        g00 = mat_in[i:i + BASE_SIZE, i:i + BASE_SIZE]
        l00 = mat_l[i:i + BASE_SIZE, i:i + BASE_SIZE] 
        l00 += cholesky_decompose(g00)
        g10 = mat_in[i + BASE_SIZE:, i:i + BASE_SIZE]
        l10 = mat_l[i + BASE_SIZE:, i:i + BASE_SIZE]
        forwardsub(l10, l00, g10)

        mat_in[i + BASE_SIZE:, i + BASE_SIZE:] -= update_remaining_submatrix(l10)


def forwardsub(l10, l00, g10):
    """calculate l10 by forward substitution"""
    g10T = NP.matrix(g10.T)
    l10T = NP.matrix(l10.T)
    for i in range(0, l10T.shape[1]):
        for j in range(0, l00.shape[1]):
            row_sum = 0
            for k in xrange(j + 1):
                if j == k:
                    l10T[k, i] += (g10T[j, i] - row_sum) / l00[j, j]
                else:
                    row_sum += l00[j, k] * l10T[k, i]

    l10 += NP.matrix(l10T.T)
    
def update_remaining_submatrix(l10):
    """updates g11"""
    return NP.matrix(l10) * NP.matrix(l10.T)
    

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
    print matrix_l
    print matrix_a.T * matrix_a
    print matrix_l * NP.matrix(matrix_l.T)

    # print NP.savetxt(out_file, matrix_out, '%20.8f')


if __name__ == '__main__':
    main(argv[1], argv[2])
