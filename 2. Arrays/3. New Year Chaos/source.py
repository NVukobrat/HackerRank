#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes_num = 0
    # end arr
    n = len(q) - 1
    if q[n - 2] > q[n - 1]:
        q[n - 2], q[n - 1] = q[n - 1], q[n - 2]  # swap
        bribes_num += 1
    if q[n - 1] > q[n]:
        q[n - 1], q[n] = q[n], q[n - 1]  # swap
        bribes_num += 1
    if q[n - 2] > q[n - 1]:
        q[n - 2], q[n - 1] = q[n - 1], q[n - 2]  # swap
        bribes_num += 1

    # rest arr
    i = n - 2
    while i > 0:
        i -= 1
        if q[i] > q[i + 1]:
            q[i], q[i + 1] = q[i + 1], q[i]  # swap
            bribes_num += 1
            if q[i + 1] > q[i + 2]:
                q[i + 1], q[i + 2] = q[i + 2], q[i + 1]  # swap
                bribes_num += 1
                if q[i + 2] > q[i + 3]:
                    bribes_num = -1
                    break
                i += 1

    if bribes_num < 0:
        print("Too chaotic")
    else:
        print(bribes_num)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
