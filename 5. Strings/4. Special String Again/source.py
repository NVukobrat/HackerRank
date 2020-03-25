#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    # II attempt
    # I attempt
    sub_num = n
    # Loop in chunks
    for chunk_size in range(2, n + 1):
        even_chunk = True if chunk_size % 2 == 0 else False
        chunk_head = 0
        while chunk_head + chunk_size <= n:
            chunk = s[chunk_head:chunk_head + chunk_size]
            chunk_head += 1

            # Odd/Even case
            if even_chunk:
                if len(set(chunk)) == 1:
                    sub_num += 1
            else:
                middle = math.floor(chunk_size / 2)
                left_half = set(chunk[:middle])
                right_half = set(chunk[middle + 1:])
                if (left_half == right_half) and ((len(left_half) == 1) and (len(right_half) == 1)):
                    sub_num += 1

    return sub_num


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
