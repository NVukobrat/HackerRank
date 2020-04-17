#!/bin/python3

import os


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    srt_arr = sorted(arr)
    min_dist = abs(srt_arr[0] - srt_arr[1])
    for i in range(1, len(srt_arr) - 1):
        diff = abs(srt_arr[i] - srt_arr[i + 1])
        if diff < min_dist:
            min_dist = diff

    return min_dist


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
