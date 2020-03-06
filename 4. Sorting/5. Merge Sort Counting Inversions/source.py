#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countInversions function below.
def countInversions(arr):
    return merge(arr)


def merge(arr):
    # Count number of inversions in order to
    # acquire swap number
    swap_num = 0

    # print("Splitting", arr)
    # Exit case
    if len(arr) < 2:
        return swap_num

    # Split halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursion calls
    swap_num += merge(left_half)
    swap_num += merge(right_half)

    # Sort halves
    index = left = right = 0
    while left < len(left_half) and right < len(right_half):
        if left_half[left] <= right_half[right]:
            arr[index] = left_half[left]
            left += 1
        elif left_half[left] > right_half[right]:
            arr[index] = right_half[right]
            right += 1
            swap_num += (middle - left)
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


# Run as PyPy3
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
