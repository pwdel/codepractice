#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    def countEach(arr):
        pluscount = 0
        minuscount = 0
        zerocount = 0
        # for each item, track if +/- or 0
        for each in range(0,len(arr)):
            if arr[each] == 0:
                zerocount = zerocount+1
            elif arr[each] > 0:
                pluscount = pluscount+1
            elif arr[each] < 0:
                minuscount = minuscount+1

        # create the instance
        posnegzero=[pluscount,minuscount,zerocount]
        # return the actual variable
        return(posnegzero)

    # create the posnegzero list instance
    posnegzeroinst = countEach(arr)

    def ratioCalculator(posnegzero,arr):
        # get the length of arr for ratio calcs
        lenarr=len(arr)
        # get each ratio
        posratio = posnegzero[0]/lenarr
        negratio = posnegzero[1]/lenarr
        zeroratio = posnegzero[2]/lenarr
        # create new ratio list
        posnegzeroratio=[posratio,negratio,zeroratio]
        return(posnegzeroratio)

    # create the instance
    posnegzeroratioinst = ratioCalculator(posnegzeroinst,arr)

    print(posnegzeroratioinst[0],'\n',posnegzeroratioinst[1],'\n',posnegzeroratioinst[2])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
