#!/bin/python3

import os
from bisect import bisect_left, insort_left


# Complete the activityNotifications function below.
def activityNotifications(d, n, expenditure):
    # ### IV attempt ###
    notification = 0
    list_d = sorted(expenditure[:d])

    for i in range(d, n):
        if expenditure[i] >= 2 * median(list_d):
            notification += 1
        del list_d[bisect_left(list_d, expenditure[i - d])]
        insort_left(list_d, expenditure[i])

    print(notification)

    # ### III attempt ###
    # end = d
    # notification = 0
    # sub_exp = expenditure[:end]
    #
    # # Position map
    # pos_map = []
    # for i in range(len(sub_exp)):
    #     pos_map.append(i)
    #
    # # First sort (Schwartzian transform)
    # sub_exp, pos_map = zip(*sorted(zip(sub_exp, pos_map)))
    # sub_exp, pos_map = list(sub_exp), list(pos_map)
    #
    # # Odd or Even
    # even = True if len(sub_exp) % 2 == 0 else False
    #
    # while end < len(expenditure):
    #     # Median
    #     if even:
    #         median = (len(sub_exp) - 1) / 2
    #         median = (sub_exp[math.ceil(median)] + sub_exp[math.floor(median)]) / 2
    #     else:
    #         median = sub_exp[len(sub_exp) // 2]
    #
    #     # Notification
    #     next_elem = expenditure[end]
    #     if next_elem >= (2 * median):
    #         notification += 1
    #
    #     # Pop
    #     # sub_exp.remove(expenditure[end - d])
    #     sub_exp.pop(pos_map[0])
    #     pos_map.pop(0)
    #
    #     # Add (Insertion sort)
    #     index = bisect.bisect(sub_exp, next_elem)
    #     sub_exp.insert(index, next_elem)
    #     pos_map.append(index)
    #
    #     end += 1
    #
    # return notification

    # ### II attempt ###
    # end = d
    # notification = 0
    #
    # # First sort
    # sub_exp = expenditure[:end]
    # sub_exp.sort()
    #
    # # Odd or Even
    # even = True if len(sub_exp) % 2 == 0 else False
    #
    # while end < len(expenditure):
    #     # Median
    #     if even:
    #         median = len(sub_exp) / 2
    #         median = (sub_exp[math.ceil(median)] + sub_exp[math.floor(median)]) / 2
    #     else:
    #         median = sub_exp[len(sub_exp) // 2]
    #
    #     # Notification
    #     next_elem = expenditure[end]
    #     if next_elem >= (2 * median):
    #         notification += 1
    #
    #     # Pop and Add (Insertion sort)
    #     sub_exp.pop(0)
    #     i = 0
    #     a = 0
    #     b = len(sub_exp)
    #     while (a + 1) < b:
    #         i = (a + b) // 2
    #         split = sub_exp[i]
    #         if split > next_elem:
    #             b = i
    #         elif split < next_elem:
    #             a = i
    #         elif split == next_elem:
    #             break
    #     sub_exp.insert(i + 1, next_elem)
    #
    #     end += 1
    #
    # return notification

    # ### I attempt ###
    # start = 0
    # end = d
    # notification = 0
    #
    # while end < len(expenditure):
    #     sub_exp = expenditure[start:end]
    #     sub_exp.sort()
    #
    #     if len(sub_exp) % 2 == 0:
    #         median = len(sub_exp) / 2
    #         median = (sub_exp[math.ceil(median)] + sub_exp[math.floor(median)]) / 2
    #     else:
    #         median = sub_exp[len(sub_exp) // 2]
    #
    #     following_elem = expenditure[end]
    #     if following_elem >= (2 * median):
    #         notification += 1
    #
    #     start += 1
    #     end += 1
    #     print(end, len(expenditure), notification)
    #
    # return notification


def median(list_d):
    return list_d[d // 2] if d % 2 == 1 else ((list_d[d // 2] + list_d[d // 2 - 1]) / 2)


if __name__ == '__main__':
    n, d = map(int, input().split())
    expenditure = list(map(int, input().split()))
    activityNotifications(d, n, expenditure)
