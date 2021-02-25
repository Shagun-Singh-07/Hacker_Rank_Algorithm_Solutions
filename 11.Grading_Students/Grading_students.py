import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grade = []
    for i in grades:
        if i<38:
            final_grade.append(str(i))
        else:
            if (int(i)+1)%5==0:
                grade = str(int(i)+1)
                final_grade.append(grade)
            elif (int(i)+2)%5==0:
                grade = str(int(i)+2)
                final_grade.append(grade)
            else:
                final_grade.append(str(i))
    return final_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
