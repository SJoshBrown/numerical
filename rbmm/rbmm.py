"""
RBMM - Recursive block matrix multipication.
By Josh Brown
CS 3513 - Numerical methods
Due - 2/10/16
"""
from sys import argv
import numpy


def validate_matrices(mat_a, mat_b):
    """
    return true if matrices are well conditioned for multipication
    """
    return mat_a.shape[1] == mat_b.shape[0]

def split(mat_a):
    """
    Takes one matrix and splits it into four quadrents, returning those
    four matrices
    """
    rows_a = mat_a.shape[0]
    cols_a = mat_a.shape[1]

    blk_a00 = mat_a[0:rows_a/2, 0:cols_a/2]
    blk_a01 = mat_a[0:rows_a/2, cols_a/2:cols_a]
    blk_a10 = mat_a[rows_a/2:rows_a, 0:cols_a/2]
    blk_a11 = mat_a[rows_a/2:rows_a, cols_a/2:cols_a]
    return [blk_a00, blk_a01, blk_a10, blk_a11]


def block_multiply(mat_a, mat_b):
    """
    Recursively split two matrices until 2x2 or smaller then multiply
    """
    if should_recurse(mat_a, mat_b):

        blk_a00, blk_a01, blk_a10, blk_a11 = split(mat_a)
        blk_b00, blk_b01, blk_b10, blk_b11 = split(mat_b)

        blk_a = block_multiply(blk_a00, blk_b00) + \
                block_multiply(blk_a01, blk_b10)
        blk_b = block_multiply(blk_a00, blk_b01) + \
                block_multiply(blk_a01, blk_b11)
        blk_c = block_multiply(blk_a10, blk_b00) + \
                block_multiply(blk_a11, blk_b10)
        blk_d = block_multiply(blk_a10, blk_b01) + \
                block_multiply(blk_a11, blk_b11)

        return NP.concatenate((NP.concatenate((blk_a, blk_b), 1),\
                               NP.concatenate((blk_c, blk_d), 1)), 0)

    else:
        return mat_a * mat_b


def should_recurse(mat_a, mat_b):
    """
    Return true if mat_a and mat_b both have dimensions greater than 2x2
    """
    return (mat_a.shape[0] > 2 or
            mat_a.shape[1] > 2 or
            mat_b.shape[0] > 2 or
            mat_b.shape[1] > 2)


NP = numpy

A = NP.loadtxt(argv[1])
B = NP.loadtxt(argv[2])

A = NP.matrix(A)
B = NP.matrix(B)

if validate_matrices(A, B):
    R = block_multiply(A, B)
    T = A*B
    print R
    print NP.testing.assert_array_almost_equal(R, T)
    NP.savetxt(argv[3], R)
    NP.savetxt('default_method.txt', T)

else:
    print ("Matrix dimension Error - Cannot take the product of a %dx%d and a "
           "%dx%d matrix.") % (A.shape[0], A.shape[1], B.shape[0], B.shape[1])
