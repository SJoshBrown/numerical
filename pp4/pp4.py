"""
PP4 - Newton's Method for Cube Root
By Josh Brown
CS 3513 - Numerical methods
Due - 4/15/16
"""
from sys import argv
import numpy
import sys
from datetime import datetime

NP = numpy
ONETHIRD = 1./3.
EP_SHIFTED = sys.float_info.epsilon * 10


def null_method(Y):
    return 1


def std_lib_method(Y):
    return Y**(1/3)


def newtons(Y):
    aOld = 0
    A = Y

    while (abs(A - aOld)/abs(A)) > (EP_SHIFTED):
        aOld = A
        A = A - ONETHIRD * (A - Y/(A*A))
    # print "set"
    # print A
    # print x**(1./3)
    return A
    
    
# def op_newtons(x):
#     a, b = math.frexp(x)
#     x1 = guess?
#     x2 = 
#     q,r = divmod(b,3)
#     return x2 * ldexp(cr, q)
    
def main():
    """
    pp4.py main function.
    """

    # test_set = NP.random.uniform(100000000, 1000000, 10000)
    test_set = NP.random.uniform(10, 100, 10)
    TEST_SET_LEN = len(test_set)
    null_result = NP.empty(10000)
    std_lib_result = NP.empty(10000)
    newtons_result = NP.empty(10000)


    start = datetime.now()
    for i in range(0, TEST_SET_LEN):
        null_result[i] = null_method(test_set[i])
    finish = datetime.now()
    print finish - start

    start = datetime.now()
    for i in range(0, TEST_SET_LEN):
        std_lib_result[i] = std_lib_method(test_set[i])
    finish = datetime.now()
    print finish - start

    start = datetime.now()
    for i in range(0, TEST_SET_LEN):
        newtons_result[i] = newtons(test_set[i])
    finish = datetime.now()
    print finish - start




if __name__ == '__main__':
    main()



# OUTPUT
# Best Time
#     Each Method (4 vals)
#     
# Ratio of best times (2 vals)
#     (tnm - tnull) / (tstd - tnull)
#     
#     (texp - tnull) / (tstd - tnull)
#     
# 2 norm-1 errors
#     ||rnm - rstd||1
#     ||rexp - rstd||1 
