#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a_occur_in_given_string = s.count('a')
    nam_of_s_repetition, sub_repetition_leftover = divmod(n, len(s))
    num_a_occur_in_sub_repetition = s[0:sub_repetition_leftover].count('a')

    return (num_a_occur_in_given_string * nam_of_s_repetition) + num_a_occur_in_sub_repetition


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
