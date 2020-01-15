#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # ### I attempt ###
    chunk_map = {}
    for n in range(1, len(s)):
        chunks = [s[i:i + n] for i in range(0, len(s)) if (i + n) <= len(s)]
        for c in chunks:
            c = ''.join(sorted(c))
            if c not in chunk_map:
                chunk_map[c] = 0
            chunk_map[c] += 1

    cleared_chunk_map = [[key, val] for key, val in chunk_map.items() if val != 1]

    anagram_num = 0
    for k, v in cleared_chunk_map:
        anagram_num += round(math.factorial(v) / (math.factorial(2) * math.factorial(v - 2)))

    return anagram_num


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
