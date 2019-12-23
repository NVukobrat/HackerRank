#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    i = 0
    while i <= (len(c) - 2):
        if c[i + 1] == 1:
            i = i + 2
            steps += 1
            continue

        try:
            if c[i + 2] == 0:
                i = i + 2
                steps += 1
                continue
        except:
            pass

        if c[i + 1] == 0:
            i = i + 1
            steps += 1
            continue

    return steps


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
