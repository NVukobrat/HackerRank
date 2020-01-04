#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp = [0] * len(arr)
    for pos, val in enumerate(arr):
        temp[val - 1] = pos

    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            swaps += 1

            t = arr[i]
            arr[i] = i + 1

            arr[temp[i]] = t
            temp[t - 1] = temp[i]

    return swaps


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
