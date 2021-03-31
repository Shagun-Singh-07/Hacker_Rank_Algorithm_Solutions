import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    yy = str(year)
    if year == 1918:
        d = 256 - 230
        return (str(d)+".09."+yy)
    elif year % 4 == 0:
        if year < 1918:
            d = 256 - 244
            return (str(d)+".09."+yy)
        else:
            if yy[2:4] == "00":
                if int(yy[0:2]) % 4 == 0:
                    d = 256 - 244
                    return (str(d)+".09."+yy)
                else:
                    d = 256 - 243
                    return (str(d)+".09."+yy)
            else:
                d = 256 - 244
                return (str(d)+".09."+yy)
    elif year % 4 != 0:
        d = 256 - 243
        return (str(d)+".09."+yy)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
