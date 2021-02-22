import math
import os
import random
import re
import sys

def plusMinus(arr):
    length = len(arr)
    plus = 0
    minus = 0
    zero = 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        elif i == 0:
            zero += 1
    positive = plus/length
    negative = minus/length
    zero_average = zero/length
    answer_positive = "{0:.6f}".format(positive)
    answer_negative = "{0:.6f}".format(negative)
    answer_zero = "{0:.6f}".format(zero_average)
    print(answer_positive)
    print(answer_negative)
    print(answer_zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
