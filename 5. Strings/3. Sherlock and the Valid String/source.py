#!/bin/python3

import os


# Complete the isValid function below.
def isValid(s):
    dc = {}
    for c in s:
        if c not in dc:
            dc[c] = 0
        dc[c] += 1

    dn = {}
    for k, v in dc.items():
        if v not in dn:
            dn[v] = 0
        dn[v] += 1

    if len(dn) == 1:
        return "YES"
    if len(dn) != 2:
        return "NO"

    min_o = min(dn)
    max_o = max(dn)
    if (max_o == 1 and dn[max_o] == 1) or (min_o == 1 and dn[min_o] == 1):
        return "YES"

    if min_o != max_o - 1:
        return "NO"

    if dn[max_o] > 1 and dn[min_o] > 1:
        return "NO"

    return "YES"


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
