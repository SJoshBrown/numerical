"""
RBMM - Recursive block matrix multiplication.
By Josh Brown
CS 3513 - Numerical methods
Due - 2/10/16
"""
from sys import argv
import numpy


def validate_matrices(mat_a, mat_b):
    """Return true if matrices are well conditioned for multipication."""
    return mat_a.shape[1] == mat_b.shape[0]


def split(mat_in):
    """
    Takes one matrix and splits it into four quadrents, returning those
    four quadrents as matrices.
    """
    rows_a = mat_in.shape[0]
    cols_a = mat_in.shape[1]

    blk_00 = mat_in[0:rows_a/2, 0:cols_a/2]
    blk_01 = mat_in[0:rows_a/2, cols_a/2:cols_a]
    blk_10 = mat_in[rows_a/2:rows_a, 0:cols_a/2]
    blk_11 = mat_in[rows_a/2:rows_a, cols_a/2:cols_a]

    return [blk_00, blk_01, blk_10, blk_11]


def block_multiply(mat_a, mat_b, mat_c):
    """
    Multiply two matrices mat_a and mat_b together using recursive block
    multiplication and adding the result to mat_c.
    """

    if should_recurse(mat_a, mat_b):
        blk_a00, blk_a01, blk_a10, blk_a11 = split(mat_a)
        blk_b00, blk_b01, blk_b10, blk_b11 = split(mat_b)
        blk_c00, blk_c01, blk_c10, blk_c11 = split(mat_c)

        block_multiply(blk_a00, blk_b00, blk_c00)
        block_multiply(blk_a01, blk_b10, blk_c00)
        block_multiply(blk_a00, blk_b01, blk_c01)
        block_multiply(blk_a01, blk_b11, blk_c01)
        block_multiply(blk_a10, blk_b00, blk_c10)
        block_multiply(blk_a11, blk_b10, blk_c10)
        block_multiply(blk_a10, blk_b01, blk_c11)
        block_multiply(blk_a11, blk_b11, blk_c11)

    else:
        mat_c += mat_a * mat_b
        return


def should_recurse(mat_a, mat_b):
    """Return true if mat_a or mat_b have dimensions greather than 2."""
    return (mat_a.shape[0] > 2 or
            mat_a.shape[1] > 2 or
            mat_b.shape[0] > 2 or
            mat_b.shape[1] > 2)


NP = numpy
A = NP.loadtxt(argv[1])
B = NP.loadtxt(argv[2])
A = NP.matrix(A)
B = NP.matrix(B)
C = NP.zeros([A.shape[0], B.shape[1]])
C = NP.matrix(C)

if validate_matrices(A, B):
    block_multiply(A, B, C)

    # TODO remove this before submitting
    T = A*B
    print C
    print NP.testing.assert_array_almost_equal(C, T)
    NP.savetxt('default_method.txt', T)

    NP.savetxt(argv[3], C)

else:
    print ("Matrix dimension Error - Cannot take the product of a %dx%d and a "
           "%dx%d matrix.") % (A.shape[0], A.shape[1], B.shape[0], B.shape[1])
