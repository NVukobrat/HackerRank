#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    row, col = len(arr), len(arr[0])
    res = []
    for a in range(row - 2):
        for b in range(col - 2):
            hg_sum = 0
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    hg_sum += arr[i][j]
            res.append(hg_sum - arr[a + 1][b] - arr[a + 1][b + 2])

    return max(res)


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
