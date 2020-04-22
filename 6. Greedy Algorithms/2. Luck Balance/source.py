#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    # Extract columns
    l = [row[0] for row in contests]
    t = [row[1] for row in contests]
    to_lose = t.count(1) - k

    # Sort them
    l, t = zip(*sorted(zip(l, t)))

    # Calc
    sum = 0
    for i in range(0, len(l)):
        if t[i] == 1 and to_lose > 0:
            to_lose -= 1
            sum -= l[i]
            continue
        sum += l[i]

    return sum


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
