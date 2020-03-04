#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countInversions function below.
def countInversions(arr):
    merge_sort(arr, list(), 0, len(arr) - 1)

    return 0


def merge_sort(array, temp, left_start, right_end):
    if left_start >= right_end:
        return
    middle = (left_start + right_end) // 2
    merge_sort(array, temp, left_start, middle)
    merge_sort(array, temp, middle + 1, right_end)
    merge_halves(array, temp, left_start, right_end)


def merge_halves(array, temp, left_start, right_end):
    left_end = (right_end + left_start) // 2
    right_start = left_end + 1

    left = left_start
    right = right_start

    while (left <= left_end) and (right <= right_end):
        if array[left] <= array[right]:
            temp.append(array[left])
            left += 1
        else:
            temp.append(array[right])
            right += 1

    temp.extend(array[left:left_end + 1])
    temp.extend(array[right:right_end + 1])

    array.clear()
    array.extend(temp)


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
