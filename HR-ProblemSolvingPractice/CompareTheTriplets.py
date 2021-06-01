# https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    intarray=[0,0]
    # Write your code here
    for each in range(0,len(a)):
        if a[each]-b[each] == 0:
            # do nothing
            pass
        elif a[each]-b[each] > 0:
            intarray[0]=intarray[0]+1
        elif a[each]-b[each] < 0:
            intarray[1]=intarray[1]+1

    return(intarray)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
