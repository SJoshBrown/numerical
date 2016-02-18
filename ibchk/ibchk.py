"""
RBMM - Iterative Block Cholesky decomposition
By Josh Brown
CS 3513 - Numerical methods
Due - 2/24/16
"""
from sys import argv
import numpy
import math

BASE_SIZE = argv[3]
NP = numpy

def cholesky_decompose(square_matrix):
    print square_matrix
    n = square_matrix.shape[0]
    newMatrix = NP.zeros([n, n])
    for i in xrange(n):
        for j in xrange(i + 1):
            line_sum = 0.0
            if i == j:
                for k in xrange(j):
                    line_sum += newMatrix[i, k] * newMatrix[i, k]
                newMatrix[i, i] = math.sqrt(square_matrix[i, i] - line_sum)
            else:
                for k in xrange(j):
                    line_sum += newMatrix[j, k] * newMatrix[i, k]
                newMatrix[i, j] = (square_matrix[i, j] - line_sum) / newMatrix[j, j]

    print newMatrix
    print NP.matrix(newMatrix) * NP.matrix(newMatrix.T)
    

def main(file_a, out_file):
    """
    Takes a matrix from file A, calculates a Gram matrix by taking A transpose
    multipied by A. Then outputs the Cholesky decomposition of that Gram matrix
    to the specified output file.
    """
    matrix_a = NP.matrix(NP.loadtxt(file_a))
    matrix_g = matrix_a.T * matrix_a
    cholesky_decompose(matrix_g)
    # print NP.savetxt(out_file, matrix_out, '%20.8f')


if __name__ == '__main__':
    main(argv[1], argv[2])
