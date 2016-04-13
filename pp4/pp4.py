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


def null(test_set, null_result):
    
    for i in range(0, len(test_set)):
        null_result[i] = 1
        
    return null_result

def main():
    """
    pp4.py main function.
    """
    
    test_set = NP.random.uniform(1000000, 100000000, 10000)
    null_result = NP.empty(10000)
    standard_result = []
    
    start = datetime.now()
    null_result = null(test_set, null_result)
    finish = datetime.now()
    
    print finish - start



if __name__ == '__main__':
    main()
