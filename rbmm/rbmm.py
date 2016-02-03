"""
RBMM - Recursive block matrix multipication.
"""
import numpy
from sys import argv

def validateMatricesForMultiplication(matA, matB):
    """
    return true if matrices are well conditioned for multipication
    """
    return matA.shape[1] == matB.shape[0]

def recursiveBlockMultiply(matA, matB):
    """
    Recursively split two matrices until 2x2 or smaller then multiply
    """
    if(matricesAreSplittable):
        rowsA = matA.shape[0]
        colsA = matA.shape[1]
        rowsB = matB.shape[0]
        colsB = matB.shape[1]
        A11 = matA[0:rowsA/2,0:colsA/2]
        A12 = matA[0:rowsA/2,colsA/2:colsA]
        A21 = matA[rowsA/2:rowsA,0:colsA/2]
        A22 = matA[rowsA/2:rowsA,colsA/2:colsA]
        B11 = matB[0:rowsB/2,0:colsB/2]
        B12 = matB[0:rowsB/2,colsB/2:colsB]
        B21 = matB[rowsB/2:rowsB,0:colsB/2]
        B22 = matB[rowsB/2:rowsB,colsB/2:colsB]

        A = A11 * B11 + A12 * B21
        B = A11 * B12 + A12 * B22
        C = A21 * B11 + A22 * B21
        D = A21 * B12 + A22 * B22
        AB = NP.concatenate((A,B), axis=1)
        CD = NP.concatenate((C,D), axis=1)
        return NP.concatenate((AB,CD), axis=0)

    return "broke"

def matricesAreSplittable(matA, matB):
    """
    Return true if matA and matB both have dimensions greater than 3x3
    """
    return True

NP = numpy

A = NP.loadtxt(argv[1])
B = NP.loadtxt(argv[2])

A = NP.matrix(A)
B = NP.matrix(B)

if validateMatricesForMultiplication(A, B):
    print "\n\n\n"
    print recursiveBlockMultiply(A, B)
    print "\n\n\n"
    print A*B
    print A*B == recursiveBlockMultiply(A, B)

else:
    print "Matrix dimension Error - Cannot take the product of a %dx%d and a %dx%d matrix." % (A.shape[0],A.shape[1],B.shape[0],B.shape[1])

def split():
    """ Split Matrix into quadrents """
    print "split"
