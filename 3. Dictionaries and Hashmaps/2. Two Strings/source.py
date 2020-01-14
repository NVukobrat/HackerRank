#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # ### II attempt ###
    common_sub = False
    s1d = {}
    for c1 in s1:
        s1d[c1] = 0

    for c2 in s2:
        if c2 in s1d:
            common_sub = True

    if common_sub:
        return "YES"
    else:
        return "NO"

    # ### I attempt ###
    # common_sub = False
    # for c1 in s1:
    #     for c2 in s2:
    #         if c1 == c2:
    #             common_sub = True
    #             break
    # if common_sub:
    #     return "YES"
    # else:
    #     return "NO"


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
