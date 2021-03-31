import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    list1 = []
    arr.sort()
    list2 = list(set(arr))
    for i in list2:
        count_item = arr.count(i)
        list1.append(count_item)
    max_list = max(list1)
    max_index = list1.index(max_list)

    maxi = list2[max_index]

    return maxi


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
