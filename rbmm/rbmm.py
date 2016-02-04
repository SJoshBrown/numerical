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
    half_rows = to_split.shape[0]/2
    half_cols = to_split.shape[1]/2

    blk_00 = to_split[:half_rows, :half_cols]
    blk_01 = to_split[:half_rows, half_cols:]
    blk_10 = to_split[half_rows:, :half_cols]
    blk_11 = to_split[half_rows:, half_cols:]

    return [blk_00, blk_01, blk_10, blk_11]


def block_multiply(mat_a, mat_b, mat_c):
    """
    Multiply two matrices mat_a and mat_b together using recursive block
    multiplication and adding the result to a pre initialized matrix mat_c.
    """

    if should_recurse(mat_a, mat_b):
        a00, a01, a10, a11 = split(mat_a)
        b00, b01, b10, b11 = split(mat_b)
        c00, c01, c10, c11 = split(mat_c)

        # If a dimension of cXX is 0 then no need to multiply
        if c00.shape[0] and c00.shape[1]:
            block_multiply(a00, b00, c00)
            block_multiply(a01, b10, c00)
        if c01.shape[0] and c01.shape[1]:
            block_multiply(a00, b01, c01)
            block_multiply(a01, b11, c01)
        if c10.shape[0] and c10.shape[1]:
            block_multiply(a10, b00, c10)
            block_multiply(a11, b10, c10)
        if c11.shape[0] and c11.shape[1]:
            block_multiply(a10, b01, c11)
            block_multiply(a11, b11, c11)

    else:
        mat_c += mat_a * mat_b


def should_recurse(mat_a, mat_b):
    """Return true if mat_a or mat_b have dimensions greather than 2."""
    return (mat_a.shape[0] > 2 or
            mat_a.shape[1] > 2 or
            mat_b.shape[0] > 2 or
            mat_b.shape[1] > 2)


def main(sys_argv):
    """
    Main function for rbmm that takes in 3 command line arguments matrixA
    matrixB and Output as text files. Mutliplies matrixA by matrixB and outputs
    to the specified output file.
    """
    NP = numpy
    matrix_a = NP.loadtxt(sys_argv[1])
    matrix_b = NP.loadtxt(sys_argv[2])
    matrix_a = NP.matrix(matrix_a)
    matrix_b = NP.matrix(matrix_b)
    matrix_c = NP.zeros([matrix_a.shape[0], matrix_b.shape[1]])

    if validate_matrices(matrix_a, matrix_b):
        block_multiply(matrix_a, matrix_b, matrix_c)
        NP.savetxt(argv[3], matrix_c)

        # TODO remove this be for submitting
        NP.savetxt('test.txt', matrix_a * matrix_b)

    else:
        print ("Matrix dimension Error - Cannot take the product of a %dx%d and"
               " a %dx%d matrix.") % (matrix_a.shape[0],
                                      matrix_a.shape[1],
                                      matrix_b.shape[0],
                                      matrix_b.shape[1])


if __name__ == '__main__':
    main(argv)
