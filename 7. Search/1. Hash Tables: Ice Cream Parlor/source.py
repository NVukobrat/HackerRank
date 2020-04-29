#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # II attempt
    # Sort
    cost_index = enumerate(cost)
    cost_index = sorted(cost_index, key=lambda a: a[1])

    # Search
    l, r = 0, len(cost) - 1
    while l <= r:
        left, right = cost_index[l], cost_index[r]
        s = left[1] + right[1]
        if money == s:
            if left[0] < right[0]:
                print(left[0] + 1,  right[0] + 1)
            else:
                print(right[0] + 1, left[0] + 1)
            break
        elif money > s:
            l += 1
        else:
            r -= 1

    # # I attempt
    # found = False
    # for i in range(len(cost)):
    #     for j in range(i + 1, len(cost)):
    #         s = cost[i] + cost[j]
    #         if s == money:
    #             print(i + 1, j + 1)
    #             found = True
    #             break
    #     if found:
    #         break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
