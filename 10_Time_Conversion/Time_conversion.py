import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_split = s.split(":")
    if "PM" in time_split[2]:
        if str(12) in time_split[0]:
            time_split[2] = time_split[2].split("PM")[0]
            time = ":".join(time_split)
        else:
            time_split[0] = str(int(time_split[0]) + 12)
            time_split[2] = time_split[2].split("PM")[0]
            time = ":".join(time_split)
    elif "AM" in time_split[2]:
        if str(12) in time_split[0]:
            time_split[0] = str(0) + str(abs(int(time_split[0]) - 12))
            time_split[2] = time_split[2].split("AM")[0]
            time = ":".join(time_split)
        else:
            time_split[2] = time_split[2].split("AM")[0]
            time = ":".join(time_split)
    return time


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
