PP3 - Point Cloud Normal Estimation
By Josh Brown
CS 3513 - Numerical methods
Due - 3/30/16

Point Cloud Normal Estimation implemented in python 2.7.10

This script takes 3 arguments.

1.  Input file A
2.  Output File
3.  k_size for local neighborhood size

Ex:  python pp3.py inputA.txt out.txt 8

This program reads in an input text file of coordinates and outputs to the
specified output file a list of points with corresponding normal unit vectors.
The points in the output file will be line separated. The components of each
point and normal vector will be separated by whitespace in the format
x y z nx ny nz.

My only real problem when developing this was getting stuck with seemingly
"almost" correct output. In the end I was slicing numpys eigenvector matrix
incorrectly as I did not realize that the eigen vectors were stored as
a column matrix.
