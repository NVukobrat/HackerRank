#!/bin/python3

import os
import sys


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    print_tree(indexes)

    return ""


def create_tree(indexes):
    root = Tree()
    root.data = 1


def print_tree(indexes):
    pass


class Tree:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


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
