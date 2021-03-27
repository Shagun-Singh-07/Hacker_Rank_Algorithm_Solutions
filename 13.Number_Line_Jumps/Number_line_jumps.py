#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        while x1 < x2:
            x1= x1 + v1
            x2= x2 + v2
        if x1 == x2:
            return("YES")
        else:
            return("NO")
    else:
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
