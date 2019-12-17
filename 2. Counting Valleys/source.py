#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    depth_level = 0
    valley_num = 0

    for d in s:
        if d == "U":
            depth_level += 1
        else:
            depth_level -= 1

        if d == "U":
            if depth_level == 0:
                valley_num += 1

    return valley_num


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
