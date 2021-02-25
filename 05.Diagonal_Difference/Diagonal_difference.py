import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    length = len(arr)
    for i in range(0,length):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][length - i - 1]
        differnece_of_diagonals = diagonal1 - diagonal2
    return abs(differnece_of_diagonals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
