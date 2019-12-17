#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = dict()

    for num in ar:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    pair_num = 0
    for key, value in count.items():
        if value != 0:
            pair_num += math.floor(value / 2)

    return pair_num


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
