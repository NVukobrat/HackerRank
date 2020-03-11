#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d = dict()
    # Until same length
    for i, j in zip(a, b):
        if i not in d:
            d[i] = 0
        d[i] += 1
        if j not in d:
            d[j] = 0
        d[j] -= 1

    # Diff length
    dl = len(a) - len(b)
    if dl == 0:
        pass
    elif dl < 0:
        for j in b[-abs(dl):]:
            if j not in d:
                d[j] = 0
            d[j] -= 1
    elif dl > 0:
        for i in b[-abs(dl):]:
            if i not in d:
                d[i] = 0
            d[i] += 1

    n = 0
    for k, v in d.items():
        n += abs(v)

    return n


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
