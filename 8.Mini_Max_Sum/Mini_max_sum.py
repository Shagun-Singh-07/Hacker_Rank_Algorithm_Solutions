import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    s = 0
    list_sum = []
    for i in arr:
        s += i
    for j in arr:
        less = s - j
        list_sum.append(less)
    list_min = min(list_sum)
    list_max = max(list_sum)

    print(list_min, list_max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
