"""
PP4 - Newton's Method for Cube Root
By Josh Brown
CS 3513 - Numerical methods
Due - 4/15/16
"""
from sys import float_info
import numpy
import math
import datetime

NP = numpy
ONE_THIRD = 1./3.
EP_SHIFTED = float_info.epsilon * 10
TWO_POW_ONE_THIRD = pow(2, 1./3)
TWO_POW_TWO_THIRD = pow(2, 2./3)


def null_method(Y):
    """Return 1 to time function call overhead"""
    return 1


def std_lib_method(Y):
    """Return the cube root of Y to time the standard method"""
    return pow(Y, ONE_THIRD)


def newtons(Y):
    """
    Return the cube root of Y using the standard newtowns method. This is
    a modified algorithm from my in class notes.
    """
    aOld = 0
    A, b = math.frexp(Y)

    while abs(A - aOld)/abs(A) > EP_SHIFTED:
        aOld = A
        A = A - ONE_THIRD * (A - Y/(A*A))

    return A


def optimized_newtons(Y):
    """
    Return the cube root of Y using Newtons method optimized for floating
    point numbers. This is a modified algorithm from the pp4part1.pdf handout.
    As well as my in class notes.
    """
    a, b = math.frexp(Y)
    rem = b % 3;

    x = (a + a) * .2063 + .5874
    x = ONE_THIRD * ( a / (x * x) + x + x)
    x = ONE_THIRD * ( a / (x * x) + x + x)
    x = ONE_THIRD * ( a / (x * x) + x + x)

    if rem == 0:
        return math.ldexp(x, b/3)
    elif rem == 1:
        return math.ldexp(x, b/3) * TWO_POW_ONE_THIRD
    else:
        return math.ldexp(x, b/3) * TWO_POW_TWO_THIRD  


def output(null_time, std_time, newtons_time, optimized_time, newtons_error,
           optimized_error, newtons_ratio, optimized_ratio):
    """Print output for pp4.py"""
    print "BEST TIMES"
    print "Best Null Time:            %s" % null_time
    print "Best Standard Method Time: %s" % std_time
    print "Best Newtons Method Time:  %s" % newtons_time
    print "Best Optimized Time:       %s" % optimized_time
    print "\nBEST TIME RATIOS"
    print "Newtons Method Ratio       %.2f" % newtons_ratio
    print "Optimized Method Ratio     %.2f" % optimized_ratio
    print "\nNORM 1 ERROR"
    print "Newtons Error              %.10f" % newtons_error
    print "Optimized Error            %.10f" % optimized_error


def main():
    """
    pp4.py main function. Calculates the cube root of 10000 floating point
    values using 3 different methods and times the results. Outputs best times,
    time ratios compared to the standard method and the norm 1 errors as with
    the results from the standard library method.
    """
    test_set = NP.random.uniform(100000000, 1000000, 10000)
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
        # NULL
        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            null_result[i] = null_method(test_set[i])
        finish = datetime.datetime.now()
        if (finish - start) < null_time:
            null_time = finish - start 

        # STANDARD LIBRARY
        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            std_lib_result[i] = std_lib_method(test_set[i])
        finish = datetime.datetime.now()
        if (finish - start) < std_time:
            std_time = finish - start 

        # NEWTONS METHOD
        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            newtons_result[i] = newtons(test_set[i])
        finish = datetime.datetime.now()
        if (finish - start) < newtons_time:
            newtons_time = finish - start 

        # OPTIMIZED METHOD
        start = datetime.datetime.now()
        for i in range(0, TEST_SET_LEN):
            optimized_result[i] = optimized_newtons(test_set[i])
        finish = datetime.datetime.now()
        if (finish - start) < optimized_time:
            optimized_time = finish - start         

    # Convert datetime.deltatime objects to float
    null_time = null_time.total_seconds()
    std_time = std_time.total_seconds()
    newtons_time = newtons_time.total_seconds()
    optimized_time = optimized_time.total_seconds()

    # Calculate Ratios
    optimized_ratio = (optimized_time - null_time) / (std_time - null_time)
    newtons_ratio = (newtons_time - null_time) / (std_time - null_time)

    # Calculate Norm 1 Errors
    newtons_error = NP.linalg.norm(newtons_result - std_lib_result, ord=1)
    optimized_error = NP.linalg.norm(optimized_result - std_lib_result, ord=1)

    # Output
    output(null_time, std_time, newtons_time, optimized_time, newtons_error, 
           optimized_error, newtons_ratio, optimized_ratio)


if __name__ == '__main__':
    main()
