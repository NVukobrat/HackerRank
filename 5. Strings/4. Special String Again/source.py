#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    # II attempt

    # Repetition pairs
    rep_list = []
    count = 0
    cur_ptr = None
    for i in range(n):
        if s[i] == cur_ptr:
            count += 1
        else:
            if cur_ptr is not None:
                rep_list.append((cur_ptr, count))
            cur_ptr = s[i]
            count = 1
    rep_list.append((cur_ptr, count))

    # Combination number of same characters
    count = 0
    for i in rep_list:
        count += (i[1] * (i[1] + 1)) // 2

    # Special char case
    for i in range(1, len(rep_list) - 1):
        if (rep_list[i - 1][0] == rep_list[i + 1][0]) and (rep_list[i][1] == 1):
            count += min(rep_list[i - 1][1], rep_list[i + 1][1])

    return count

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
