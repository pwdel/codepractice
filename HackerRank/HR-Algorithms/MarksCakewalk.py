# https://www.hackerrank.com/challenges/marcs-cakewalk/problem

# hint - he can eat the cupcakes in any order.
# we're looking for the *minimum* - which means we need to order from greatest to least to start off

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # write your code here

    # sort and reverse the calorie list
    calorierev = sorted(calorie,reverse=True)
    # set previous to 0 to start off with
    previous = 0

    # for each
    for i in range(0,len(calorierev)):
        # current value
        current=(2**i)*calorierev[i]
        # previous value
        previous=previous+current

    return(previous)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
