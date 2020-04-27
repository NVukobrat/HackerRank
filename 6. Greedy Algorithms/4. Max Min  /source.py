#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    sort_arr = sorted(arr)

    min_unfairness = sort_arr[k - 1] - sort_arr[0]
    for i in range(1, len(sort_arr) - k + 1):
        unfairness = sort_arr[i + k - 1] - sort_arr[i]
        if min_unfairness > unfairness:
            min_unfairness = unfairness

    return min_unfairness


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
