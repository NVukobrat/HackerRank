#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countInversions function below.
def countInversions(arr):
    swap_num = merge(arr, 0)

    return swap_num


def merge(arr, swap_num):
    # print("Splitting", arr)
    # Exit case
    if len(arr) < 2:
        return

    # Split halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursion calls
    merge(left_half, swap_num)
    merge(right_half, swap_num)

    # Sort halves
    index = left = right = 0
    while left < len(left_half) and right < len(right_half):
        if left_half[left] < right_half[right]:
            arr[index] = left_half[left]
            left += 1
        elif left_half[left] > right_half[right]:
            arr[index] = right_half[right]
            right += 1
        index += 1

    # Populate rest
    while left < len(left_half):
        arr[index] = left_half[left]
        left += 1
        index += 1
    while right < len(right_half):
        arr[index] = right_half[right]
        right += 1
        index += 1

    # print("Merging ", arr)
    return swap_num


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
