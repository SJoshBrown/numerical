RBMM - Recursive block matrix multiplication.
By Josh Brown
CS 3513 - Numerical methods
Due - 2/10/16

Recursive block matrix multiplication implemented in python 2.7.10

This script takes 3 arguments.

1.  Input file A
2.  Input file B
3.  Output file

Ex:  python rbmm.py inputA.txt inputB.txt out.txt

It reads in one matrix each from files A and B multiplies them and
outputs the result to the output file.

I debated whether or not to use the conditional statements inside
the block_multiply function that check for a zero dimension of CXX.
After some testing the script seems to run at approximately the same
speed regardless of whether or not they are included. However, I
decided to keep them in as it was mentioned during class that numpy
had gone back and forth on how to handle matrices with a zero
dimension.
