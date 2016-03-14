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


def main(in_file, out_file, k_size):
    """
    main
    """

    points = NP.loadtxt(in_file)
    k_points = k_closest_points(points, points[0], k_size)
    print k_points



if __name__ == '__main__':
    try:
        int(argv[3])
        K_SIZE = int(argv[3])
    except (ValueError, IndexError):
        print "Error - invalid arguments"
    main(argv[1], argv[2], K_SIZE)
