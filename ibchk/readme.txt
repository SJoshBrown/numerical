IBCHK - Iterative Block Cholesky Decomposition
By Josh Brown
CS 3513 - Numerical methods
Due - 2/24/16

Iterative block matrix decomposition implemented in python 2.7.10

This script takes 3 arguments.

1.  Input file A
2.  Output File
3.  Base Size for block decomposition (optional)

Ex:  python ibchk.py inputA.txt out.txt 5

It reads in one matrix and decomposes it into the lower triangular
Cholesky decomposition matrix L. Then outputs L to the specified
output file.

If no Base Size is specified for the 3rd argument a default size
of 8 will be used.
