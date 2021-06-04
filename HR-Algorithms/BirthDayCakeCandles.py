# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen

# hint - you might need to convert outputs into integers when passing from function to function

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    def determinemMax(candles):
        maxcandle = max(candles)
        return(maxcandle)

    maxcandle_inst = int(determinemMax(candles))

    def countMaxes(candles,maxcandlevalue):
        blownoutcount=0
        for each in range(0,len(candles)):
            if candles[each] == maxcandlevalue:
                blownoutcount=blownoutcount+1

        return(blownoutcount)

    blownoutcount_inst = int(countMaxes(candles,maxcandle_inst))

    return(blownoutcount_inst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
