"""
PP4 - Newton's Method for Cube Root
By Josh Brown
CS 3513 - Numerical methods
Due - 4/15/16
"""
from sys import argv
import numpy
import sys
import math
import datetime

NP = numpy
ONETHIRD = 1./3.
EP_SHIFTED = sys.float_info.epsilon * 10
TWO_POW_ONE_THIRD = 2**(1./3)
TWO_POW_TWO_THIRD = 2**(2./3)


def null_method(Y):
    return 1


def std_lib_method(Y):
    return Y**(1./3)


def newtons(Y):
    aOld = 0
    A = Y

    while (abs(A - aOld)/abs(A)) > (EP_SHIFTED):
        aOld = A
        A = A - ONETHIRD * (A - Y/(A*A))
    return A


def optimized_newtons(Y):
    a, b = math.frexp(Y)
    rem = b % 3;

    x1 = .7937 + ((2 * a) - 1) * (.2063)
    x2 = (1./3.) * (( a / (x1 * x1)) + (2 * x1 ))
    x2 = (1./3.) * (( a / (x2 * x2)) + (2 * x2 ))
    x2 = (1./3.) * (( a / (x2 * x2)) + (2 * x2 ))

    if rem == 0:
        return math.ldexp(x2, b/3)
    elif rem == 1:
        return math.ldexp(x2, b/3) * TWO_POW_ONE_THIRD
    else:
        return math.ldexp(x2, b/3) * TWO_POW_TWO_THIRD  


def output(null_time, std_time, newtons_time, optimized_time, newtons_error,
           optimized_error, newtons_ratio, optimized_ratio):
    print "\n" * 3
    print "BEST TIMES"
    print "Best Null Time:            %s" % null_time
    print "Best Standard Method Time: %s" % std_time
    print "Best Newtons Method Time:  %s" % newtons_time
    print "Best Optimized Time:       %s" % optimized_time
    print "\nBEST TIME RATIOS"
    print "Newtons Method Ratio       %s" % newtons_ratio
    print "Optimized Method Ratio     %s" % optimized_ratio
    print "\nNORM 1 ERROR"
    print "Newtons Error              %.15f" % newtons_error
    print "Optimized Error            %.15f" % optimized_error


def main():
    """
    pp4.py main function.
    """

    test_set = NP.random.uniform(100000000, 1000000, 10000)
    # test_set = NP.random.uniform(10, 100, 10)
    TEST_SET_LEN = len(test_set)
    null_result = NP.empty(10000)
    std_lib_result = NP.empty(10000)
    newtons_result = NP.empty(10000)
    optimized_result = NP.empty(10000)

    null_time = datetime.timedelta(1)
    std_time = datetime.timedelta(1)
    newtons_time = datetime.timedelta(1)
    optimized_time = datetime.timedelta(1)

    for i in range(0, 10):
        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            null_result[i] = null_method(test_set[i])
        finish = datetime.datetime.now()
        print finish - start
        if (finish - start) < null_time:
            null_time = finish - start 
        print null_time

        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            std_lib_result[i] = std_lib_method(test_set[i])
        finish = datetime.datetime.now()
        print finish - start
        if (finish - start) < std_time:
            std_time = finish - start 

        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            newtons_result[i] = newtons(test_set[i])
        finish = datetime.datetime.now()
        print finish - start
        if (finish - start) < newtons_time:
            newtons_time = finish - start 

        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            optimized_result[i] = optimized_newtons(test_set[i])
        finish = datetime.datetime.now()
        print finish - start
        if (finish - start) < optimized_time:
            optimized_time = finish - start         
    

    # Convert datetime.deltatime objects to float
    null_time = null_time.total_seconds()
    std_time = std_time.total_seconds()
    newtons_time = newtons_time.total_seconds()
    optimized_time = optimized_time.total_seconds()

    optimized_ratio = (optimized_time - null_time) / (std_time - null_time)
    newtons_ratio = (newtons_time - null_time) / (std_time - null_time)

    newtons_error = NP.linalg.norm(newtons_result - std_lib_result, ord=1)
    optimized_error = NP.linalg.norm(optimized_result - std_lib_result, ord=1)

    output(null_time, std_time, newtons_time, optimized_time, newtons_error, 
           optimized_error, newtons_ratio, optimized_ratio)


if __name__ == '__main__':
    main()
