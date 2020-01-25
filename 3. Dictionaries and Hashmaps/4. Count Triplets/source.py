#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    # ### II attempt ###
    triplet_count = 0
    before = {}
    after = {}

    # Set element before
    before[arr[0]] = 1

    # Set elements after
    for i in range(2, len(arr)):
        after[arr[i]] = after.get(arr[i], 0) + 1

    for i in range(1, len(arr) - 1):
        # Count triplets if satisfy geometrical progression
        if ((arr[i] / r) in before) and ((arr[i] * r) in after):
            triplet_count += before[arr[i] / r] * after[arr[i] * r]

        # Populate elements before
        before[arr[i]] = before.get(arr[i], 0) + 1

        # Neglect utilize elements
        after[arr[i + 1]] -= 1

    return triplet_count

    # ### I attempt ###
    #
    # Count occurrence
    # geo_dict = {}
    # for num in arr:
    #     if num not in geo_dict:
    #         geo_dict[num] = 0
    #     geo_dict[num] += 1
    #
    # # Remove invalid geometrical progression elements.
    # for_removal = []
    # prev_elem = None
    # for k, v in geo_dict.items():
    #     if prev_elem is None:
    #         prev_elem = k
    #         continue
    #     if (prev_elem * r) != k:
    #         for_removal.append(k)
    #     else:
    #         prev_elem = k
    # for e in for_removal:
    #     del geo_dict[e]
    #
    # # Count triplets
    # triplet_num = 0
    # if len(geo_dict) == 1:
    #     for k, v in geo_dict.items():
    #         triplet_num += round(math.factorial(v) / (6 * math.factorial(v - 3)))  # combinations
    # else:
    #     triplets = []
    #     for k, v in geo_dict.items():
    #         triplets.append(v)
    #
    #         if len(triplets) == 3:
    #             mul_res = 1
    #             for t in triplets:
    #                 mul_res *= t
    #             triplet_num += mul_res
    #             triplets.pop(0)
    #
    # return triplet_num


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
