# https://www.hackerrank.com/challenges/insertionsort1/problem

# hint - need to print off values rather than the list itself.
# this can be accomplished with "print(*arr)" rather than "print(arr)"
# need a stop flag to tell when to stop sorting
# we're going backwards, so it's a len(thing)-i scenario
# always inserting the value "one prior"
# watch out for case where the number given will get sorted all the way down to the bottom.

# hint - the mechanics of this type of problem in terms of how to set indexes are very persnickity.
# it was helpful to print out exactly what was happening for each operation as it happened.
# the printed signals should be removed in order to submit successfully to hackerrank.
# however running the program with the prints may help with understanding what is going on.
# printed out version can be found at InsertionSortHint.py

# input:
# 2 3 4 5 6 7 8 9 10 1

# output:
# 2 3 4 5 6 7 8 9 10 10
# 2 3 4 5 6 7 8 9 9 10
# 2 3 4 5 6 7 8 8 9 10
# 2 3 4 5 6 7 7 8 9 10
# 2 3 4 5 6 6 7 8 9 10
# 2 3 4 5 5 6 7 8 9 10
# 2 3 4 4 5 6 7 8 9 10
# 2 3 3 4 5 6 7 8 9 10
# 2 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    # n appears to be the length of the vector
    # original last value
    value = arr[n-1]
    # stop flag
    flag=0
    for i in range(0,len(arr)):
        # checkpoint, work backwards
        # we have to start 2 previous to the end because 1 previous to end is the value
        # hence the, "-2" in the calculation for checkpoint "c"
        c = len(arr)-i-2
        # if have not hit a stop flag yet
        # and if our given value is less than the current checkpoint
        if value < arr[c] and flag == 0:
            # special case - we're at c=-1, the end
            if c==-1:
              # set the first index to value
              arr[0]=value
            else:
              # move the value at c to the right
              # hence c+1, the value to the right of c being shifted
              arr[c+1]=arr[c]
            # display arr
            print(*arr)
        # if value is now greater than our moving left checkpoint, still no stop flag
        elif value > arr[c] and flag == 0:
            # we have basically found the stop point
            # because our value is now greater than the checkpoint value
            # put the original value in location to right
            arr[c+1]=value
            # if not through with list yet, basically if i is not at the array end
            if i<len(arr):
                # set a stop flag
                flag=1
            else:
                # otherwise keep going
                flag=0
            # print it out
            print (*arr)
        # case where stopflag has occured, don't do anything
        elif flag == 1:
            # do nothing
            pass


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
