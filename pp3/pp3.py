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
    distance_list = {}
    k_points = []

    # Calculate all distances and add to a dict of [index, distance]
    for i in range(0, len(points)):
        distance_list[str(i)] = NP.linalg.norm(center_point - points[i])

    # Throw away first min. This is the point we are centered on.
    key = min(distance_list, key=distance_list.get)
    del[distance_list[key]]

    for i in range(0, k):
        key = min(distance_list, key=distance_list.get)
        k_points.append(points[int(key)])
        del[distance_list[key]]

    return k_points


def zero_mean(points):
    n = len(points)
    x = 0
    y = 0
    z = 0
    for i in range(0, n):
        x += points[i][0]
        y += points[i][1]
        z += points[i][2]
    mean = [x/n, y/n, z/n]

    centered_points = []

    for i in range(0,len(points)):
        centered_points.append(points[i] - mean)
    return centered_points


def estimate_normal(points, k_points, center_point):
    """estimate normal"""
    # Add the point we are considering back into the list to calculate on k + 1
    k_points.append(center_point)

    centered_points = NP.matrix(zero_mean(k_points))

    cov_mat = (centered_points.T * centered_points)/(len(k_points) - 1)
    w, v  = NP.linalg.eig(cov_mat)

    min_val = min(w)
    index = NP.where(w == min_val)
    print "%s, %s" % (center_point, v[index])



def main(in_file, out_file, k_size):
    """
    main
    """

    points = NP.loadtxt(in_file)
    for i in range(0, len(points)):
        k_points = k_closest_points(points, points[i], k_size)
        estimate_normal(points, k_points, points[i])


if __name__ == '__main__':
    try:
        int(argv[3])
        K_SIZE = int(argv[3])
    except (ValueError, IndexError):
        print "Error - invalid arguments"
    main(argv[1], argv[2], K_SIZE)
