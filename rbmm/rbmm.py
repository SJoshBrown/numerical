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
    if(matricesAreSplittable(matA,matB)):
        rowsA = matA.shape[0]
        colsA = matA.shape[1]
        rowsB = matB.shape[0]
        colsB = matB.shape[1]
        A00 = matA[0:rowsA/2,0:colsA/2]
        A01 = matA[0:rowsA/2,colsA/2:colsA]
        A10 = matA[rowsA/2:rowsA,0:colsA/2]
        A11 = matA[rowsA/2:rowsA,colsA/2:colsA]
        B00 = matB[0:rowsB/2,0:colsB/2]
        B01 = matB[0:rowsB/2,colsB/2:colsB]
        B10 = matB[rowsB/2:rowsB,0:colsB/2]
        B11 = matB[rowsB/2:rowsB,colsB/2:colsB]

        A = recursiveBlockMultiply(A00,B00) + recursiveBlockMultiply(A01, B10)
        B = recursiveBlockMultiply(A00,B01) + recursiveBlockMultiply(A01, B11)
        C = recursiveBlockMultiply(A10,B00) + recursiveBlockMultiply(A11, B10)
        D = recursiveBlockMultiply(A10,B01) + recursiveBlockMultiply(A11, B11)
        AB = NP.concatenate((A,B), axis=1)
        CD = NP.concatenate((C,D), axis=1)
        return NP.concatenate((AB,CD), axis=0)

    else:
        rowsA = matA.shape[0]
        colsA = matA.shape[1]
        rowsB = matB.shape[0]
        colsB = matB.shape[1]
        A00 = matA[0:rowsA/2,0:colsA/2]
        A01 = matA[0:rowsA/2,colsA/2:colsA]
        A10 = matA[rowsA/2:rowsA,0:colsA/2]
        A11 = matA[rowsA/2:rowsA,colsA/2:colsA]
        B00 = matB[0:rowsB/2,0:colsB/2]
        B01 = matB[0:rowsB/2,colsB/2:colsB]
        B10 = matB[rowsB/2:rowsB,0:colsB/2]
        B11 = matB[rowsB/2:rowsB,colsB/2:colsB]

        A = A00 * B00 + A01 * B10
        B = A00 * B01 + A01 * B11
        C = A10 * B00 + A11 * B10
        D = A10 * B01 + A11 * B11

        AB = NP.concatenate((A,B), axis=1)
        CD = NP.concatenate((C,D), axis=1)
        return NP.concatenate((AB,CD), axis=0)

def matricesAreSplittable(matA, matB):
    """
    Return true if matA and matB both have dimensions greater than 3x3
    """
    splittable = False;
    if(matA.shape[0] > 3 and matA.shape[1] > 3 and matB.shape[0] > 3 and matB.shape[1] > 3):
        splittable = True;
    return splittable

NP = numpy

A = NP.loadtxt(argv[1])
B = NP.loadtxt(argv[2])

A = NP.matrix(A)
B = NP.matrix(B)

if validateMatricesForMultiplication(A, B):
    R = recursiveBlockMultiply(A,B)
    T = A*B
    print R
    print NP.testing.assert_array_almost_equal(R, T, 9)


else:
    print "Matrix dimension Error - Cannot take the product of a %dx%d and a %dx%d matrix." % (A.shape[0],A.shape[1],B.shape[0],B.shape[1])
