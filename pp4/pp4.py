"""
PP4 - Newton's Method for Cube Root
By Josh Brown
CS 3513 - Numerical methods
Due - 4/15/16
"""
from sys import argv
import numpy
from datetime import datetime

NP = numpy


def null_method(x):
    return 1
    
def std_lib_method(x):
    return x**(1/3)
    

def main():
    """
    pp4.py main function.
    """
    
    test_set = NP.random.uniform(1000000, 100000000, 10000)
    TEST_SET_LEN = len(test_set)
    null_result = NP.empty(10000)
    std_lib_result = NP.empty(10000)


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




if __name__ == '__main__':
    main()
