import math
import os
import random
import re
import sys

def birthday(s, d, m):
    list1 = []
    if m == 1:
        for i in s:
            if i == d:
                list1.append(i)
        if len(list1) == 0:
            return "0"
        else:
            return len(list1)
    else:
        for i,j in zip(range(0,len(s)),range(m,len(s)+2)):
            addition = sum(s[i:j])
            if addition == d:
                list1.append(addition)
        return len(list1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
