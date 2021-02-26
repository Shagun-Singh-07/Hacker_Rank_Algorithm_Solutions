import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_for_apple = 0
    count_for_orange = 0
    for i in apples:
        if (int(i)+int(a))>=int(s) and (int(i)+int(a))<=int(t):
            count_for_apple += 1
        else:
            pass
    for i in oranges:
        if (int(i)+int(b))>=int(s) and (int(i)+int(b))<=int(t):
            count_for_orange += 1
        else:
            pass
    print(count_for_apple)
    print(count_for_orange)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
