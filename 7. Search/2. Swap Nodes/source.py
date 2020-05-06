#!/bin/python3

depth = {}
left = []
right = []


def depth_order(value, d=1):
    if d not in depth.keys():
        depth[d] = []
    depth[d].append(value)
    if left[value] >= 0:
        depth_order(left[value], d + 1)
    if right[value] >= 0:
        depth_order(right[value], d + 1)


def in_order(value):
    if left[value] >= 0:
        in_order(left[value])
    print(value + 1, end=" ")
    if right[value] >= 0:
        in_order(right[value])


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x = list(map(int, input().rstrip().split()))
        left.append(x[0] - 1)
        right.append(x[1] - 1)

    root = 0
    depth_order(root)
    queries_count = int(input())

    for _ in range(queries_count):
        queries_item = int(input())
        for j in range(queries_item, len(depth), queries_item):
            for value in depth[j]:
                left[value], right[value] = right[value], left[value]
        in_order(root)
        print()
