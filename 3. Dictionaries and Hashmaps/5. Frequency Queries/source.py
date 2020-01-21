#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    # ### III attempt ###
    num_freq = {}
    freq_freq = {}
    result = []
    for q in queries:
        command, value = q
        cur_freq = num_freq.get(value, 0)
        new_freq = 0
        if command == 1:
            new_freq = cur_freq + 1
        if command == 2:
            new_freq = cur_freq - 1 if cur_freq > 0 else 0
        if command == 1 or command == 2:
            num_freq[value] = new_freq
            if cur_freq in freq_freq:
                freq_freq[cur_freq] -= 1 if freq_freq[cur_freq] > 0 else 0
            if num_freq[value] not in freq_freq:
                freq_freq[num_freq[value]] = 0
            freq_freq[num_freq[value]] += 1
        if command == 3:
            if value in freq_freq:
                result.append(1 if freq_freq[value] > 0 else 0)
            else:
                result.append(0)

    return result

    # ### II attempt ###
    # num_freq = {}
    # freq_freq = {}
    # result = []
    # for q in queries:
    #     command, value = q
    #     cur_freq = num_freq.get(value, 0)
    #     if command == 1:
    #         new_freq = cur_freq + 1
    #         num_freq[value] = new_freq
    #         if cur_freq in freq_freq:
    #             freq_freq[cur_freq] -= 1 if freq_freq[cur_freq] > 0 else 0
    #         if new_freq not in freq_freq:
    #             freq_freq[new_freq] = 0
    #         freq_freq[new_freq] += 1
    #     elif command == 2:
    #         new_freq = cur_freq - 1 if cur_freq > 0 else 0
    #         num_freq[value] = new_freq
    #         if cur_freq in freq_freq:
    #             freq_freq[cur_freq] -= 1 if freq_freq[cur_freq] > 0 else 0
    #         if num_freq[value] not in freq_freq:
    #             freq_freq[num_freq[value]] = 0
    #         freq_freq[num_freq[value]] += 1
    #     else:
    #         if value in freq_freq:
    #             result.append(1 if freq_freq[value] > 0 else 0)
    #         else:
    #             result.append(0)
    #
    # return result

    # ### I attempt ###
    # dict_structure = {}
    # result = []
    # for q in queries:
    #     command, value = q
    #     if command == 1:
    #         if value not in dict_structure:
    #             dict_structure[value] = 0
    #         dict_structure[value] += 1
    #     elif command == 2:
    #         if value in dict_structure:
    #             dict_structure[value] -= 1
    #             if dict_structure[value] == 0:
    #                 dict_structure.pop(value)
    #     else:
    #         occurrence = False
    #         for i in dict_structure.values():
    #             if i == value:
    #                 occurrence = True
    #                 break
    #         if occurrence:
    #             result.append(1)
    #         else:
    #             result.append(0)
    #
    # return result


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
