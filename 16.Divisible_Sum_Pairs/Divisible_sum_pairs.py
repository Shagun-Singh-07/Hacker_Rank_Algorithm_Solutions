import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    list1 = []
    for i in range(0,len(ar)):
        for j in range(0,len(ar)):
            if i < j:
                sum_of_array = ar[i] + ar[j]
                if sum_of_array % k == 0:
                    list1.append(sum_of_array)
    return len(list1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
