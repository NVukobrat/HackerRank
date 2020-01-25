#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    sum = 0
    num_prices = 0
    for i in range(len(prices)):
        min_price = min(prices)
        prices.remove(min_price)
        sum += min_price
        if sum > k:
            break
        num_prices += 1

    return num_prices


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
