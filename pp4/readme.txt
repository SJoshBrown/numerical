PP4 - Newton's Method for Cube Root
By Josh Brown
CS 3513 - Numerical methods
Due - 4/15/16

Newton's Method for Cube Root implemented in python 2.7.10

Usage:  python pp4.py

This script creates 10000 floating point values between 1 million
and 100 million and then times 3 different methods for calculating
the cube root on them.

The three methods are the standard library function pow(), Newton's
method and an optimized version of Newton's method.

The output shows the best times for each of the 3 methods as well
as a null time that simulates the function call overhead. It also
displays the error norms for Newton's method as well as the optimized
version of Newton's method.

BEST TIMES
Best Null Time:            0.00207
Best Standard Method Time: 0.004454
Best Newtons Method Time:  0.229049
Best Optimized Time:       0.01466

BEST TIME RATIOS
Newtons Method Ratio       95.21
Optimized Method Ratio     5.28

NORM 1 ERROR
Newtons Error              0.0000000011
Optimized Error            0.0000000021
