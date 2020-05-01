#!/bin/python3

import os
import sys


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    # Construct full binary tree
    i = 0
    stop_progress = 0
    stop_goal = len(indexes)
    while i < len(indexes):
        new_i = None
        if indexes[i][0] in {-1, "*"}:
            new_i = (i * 2) + 1
        if indexes[i][1] in {-1, "*"}:
            new_i = (i + 1) * 2
        if indexes[i][0] not in {"*"} or indexes[i][1] not in {"*"}:
            stop_progress += 1
        if new_i is not None:
            indexes.insert(new_i, ('*', '*'))
        i += 1

        if stop_progress == stop_goal:
            break

    # TODO: Error above [case with parent of 10, 11]
    # Print tree
    depth = 1
    added = 0
    print(1)
    for r, l in indexes:
        # print()
        print(r if r != -1 else "*", l if l != -1 else "*", end=' ')
        added += 2
        if added == depth * 2:
            depth *= 2
            added = 0
            print()

    return ""


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "out.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
