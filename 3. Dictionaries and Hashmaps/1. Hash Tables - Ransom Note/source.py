#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_map = {}
    possible = True
    for n in note:
        if n not in note_map:
            note_map[n] = 0
        note_map[n] += 1

    for m in magazine:
        if m not in note_map:
            continue
        note_map[m] -= 1

    for nm in note_map:
        if note_map[nm] > 0:
            possible = False
            break

    if possible:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
