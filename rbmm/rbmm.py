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


def split(to_split):
    """
    Takes one matrix and splits it into four quadrents, returning those
    four quadrents as slices of the input matrix.
    """
    rows = to_split.shape[0]
    cols = to_split.shape[1]

    blk_00 = to_split[:rows/2, :cols/2]
    blk_01 = to_split[:rows/2, cols/2:]
    blk_10 = to_split[rows/2:, :cols/2]
    blk_11 = to_split[rows/2:, cols/2:]

    return [blk_00, blk_01, blk_10, blk_11]


def block_multiply(mat_a, mat_b, mat_c):
    """
    Multiply two matrices mat_a and mat_b together using recursive block
    multiplication and adding the result to mat_c.
    """

    if should_recurse(mat_a, mat_b):
        a00, a01, a10, a11 = split(mat_a)
        b00, b01, b10, b11 = split(mat_b)
        c00, c01, c10, c11 = split(mat_c)

        block_multiply(a00, b00, c00)
        block_multiply(a01, b10, c00)
        block_multiply(a00, b01, c01)
        block_multiply(a01, b11, c01)
        block_multiply(a10, b00, c10)
        block_multiply(a11, b10, c10)
        block_multiply(a10, b01, c11)
        block_multiply(a11, b11, c11)

    else:
        mat_c += mat_a * mat_b
        return


def should_recurse(mat_a, mat_b):
    """Return true if mat_a or mat_b have dimensions greather than 2."""
    return (mat_a.shape[0] > 2 or
            mat_a.shape[1] > 2 or
            mat_b.shape[0] > 2 or
            mat_b.shape[1] > 2)


def main(sys_argv):
    """
    Main function that takes in 3 command line arguments matrixA matrixB
    and Output. Mutliplies matrixA by matrixB and outputs to the specified
    output file.
    """
    NP = numpy
    A = NP.loadtxt(sys_argv[1])
    B = NP.loadtxt(sys_argv[2])
    A = NP.matrix(A)
    B = NP.matrix(B)
    C = NP.zeros([A.shape[0], B.shape[1]])

    if validate_matrices(A, B):
        block_multiply(A, B, C)
        NP.savetxt(argv[3], C)

        # TODO remove this be for submitting
        NP.savetxt('test.txt', A*B)

    else:
        print ("Matrix dimension Error - Cannot take the product of a %dx%d and a "
               "%dx%d matrix.") % (A.shape[0], A.shape[1], B.shape[0], B.shape[1])


if __name__ == '__main__':
    main(argv)
