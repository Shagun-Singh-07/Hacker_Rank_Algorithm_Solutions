#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    max = 0
    min = 0
    max_number = scores[0]
    min_number = scores[0]
    for i in scores:
        if i > max_number:
            max_number = i
            max += 1
        elif i < min_number:
            min_number = i
            min += 1
    return (max, min)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
