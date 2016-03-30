"""
PP3 - Point Cloud Normal Estimation
By Josh Brown
CS 3513 - Numerical methods
Due - 3/30/16
"""
from sys import argv
import numpy

NP = numpy


def k_closest_points(points, center_point, k):
    """
    returns the k + 1 closest points to the center point param
    """
    distance_list = {}
    k_points = []

    # Calculate all distances and add to a dict of [index, distance]
    for i in range(0, len(points)):
        distance_list[str(i)] = NP.linalg.norm(center_point - points[i])

    for i in range(0, k + 1):
        key = min(distance_list, key=distance_list.get)
        k_points.append(points[int(key)])
        del[distance_list[key]]

    return k_points


def zero_mean(points):
    """
    Takes a set of points as a param and returns a new set based on the param
    that have been centered around a zero mean
    """
    mean = calc_centroid(points)
    centered_points = []

    for i in range(0,len(points)):
        centered_points.append(points[i] - mean)
    return centered_points


def estimate_normal(k_points):
    """
    Takes a set of points and first calculates the covariance matrix. Then
    returns the eigenvector associated with the smallest eigen value for that
    matrix.
    """
    centered_points = NP.matrix(zero_mean(k_points))

    cov_mat = (centered_points.T * centered_points)/(len(k_points))
    e_val, e_vec  = NP.linalg.eig(cov_mat)

    min_index = NP.argmin(e_val)

    return  NP.asarray(e_vec[:,min_index])


def calc_centroid(points):
    """
    Take a set of points as an argument and returns the centroid for those
    points.
    """
    n = len(points)

    x = 0
    y = 0
    z = 0
    for i in range(0, n):
        x += points[i][0]
        y += points[i][1]
        z += points[i][2]
    centroid = [x/n, y/n, z/n]
    return centroid


def main(in_file, out_file, k_size):
    """
    pp3.py main function. Takes 3 CLI arguments in_file, out_file and k size.
    pp3 calculates normal estimations based on nearest neighbor point clouds
    of size k.
    """
    points = NP.loadtxt(in_file)
    centroid = calc_centroid(points)
    normals = []
    for i in range(0, len(points)):
        print i
        k_points = k_closest_points(points, points[i], k_size)
        norm = estimate_normal(k_points)
        if NP.dot((points[i] - centroid), norm) < 0:
            norm = norm * -1
        
        normals.append(norm.reshape(1,3)[0])

    output = NP.concatenate((points, normals), axis=1)
    NP.savetxt(out_file, output)

if __name__ == '__main__':
    try:
        int(argv[3])
        K_SIZE = int(argv[3])
    except (ValueError, IndexError):
        print "Error - invalid arguments"
    main(argv[1], argv[2], K_SIZE)
