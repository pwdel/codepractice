# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxscore=scores[0]
    maxbroken=0
    minscore=scores[0]
    minbroken=0
    for i in range(0,len(scores)):
        if scores[i] > maxscore:
            maxscore=scores[i]
            maxbroken=maxbroken+1
        elif scores[i] < minscore:
            minscore=scores[i]
            minbroken=minbroken+1

    return(maxbroken,minbroken)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
