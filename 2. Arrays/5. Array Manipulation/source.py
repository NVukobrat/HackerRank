#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # ### III attempt ###
    a = [0] * (n + 1)
    for p, q, s in queries:
        a[p] += s
        if q + 1 <= n:
            a[q + 1] -= s

    x = 0
    m = 0
    for i in range(n + 1):
        x += a[i]
        if m < x:
            m = x

    return m

    # ### II attempt ###
    # intersections = []
    # new_intersections = []
    # for i in range(len(queries)):
    #     x, y, v = queries[i]
    #     case_activated = False
    #     if not intersections:
    #         intersections.append([x, y, v])
    #         continue
    #     for ii in range(len(intersections)):
    #         xi, yi, vi = intersections[ii]
    #         # III
    #         if (xi < x < yi) and (xi < y < yi):
    #             new_intersections.append([xi, x, vi])
    #             new_intersections.append([y, yi, vi])
    #             intersections[ii][0] = x
    #             intersections[ii][1] = y
    #             intersections[ii][2] += v
    #             case_activated = True
    #         # I
    #         elif xi < y < yi:
    #             new_intersections.append([x, xi, v])
    #             new_intersections.append([xi, y, v + vi])
    #             intersections[ii][0] = y
    #             case_activated = True
    #         # II
    #         elif xi < x < yi:
    #             new_intersections.append([xi, x, vi])
    #             new_intersections.append([x, yi, v + vi])
    #             intersections[ii][1] = x
    #             case_activated = True
    #         # IV
    #         elif (xi > x) and (yi < y):
    #             intersections[ii][0] = x
    #             intersections[ii][1] = y
    #             intersections[ii][2] += v
    #             case_activated = True
    #     # V
    #     if not case_activated:
    #         new_intersections.append([x, y, v])
    #
    #     intersections += new_intersections
    #     new_intersections = []
    #
    # max_intersection_val = 0
    # for x, y, v in intersections:
    #     if v > max_intersection_val:
    #         max_intersection_val = v
    #
    # return max_intersection_val

    # ### I attempt ###
    # sum_arr = [0] * n
    # for row in queries:
    #     for i in range(row[0] - 1, row[1]):
    #         sum_arr[i] += row[2]
    # return max(sum_arr)


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
