# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here

    # find all pairs, put in overall list
    indexlist=[]
    # remslice pairs to get full list
    for i in range(0,n):
        # values of slice previous to i
        # we don't use values previous to i, we just look forward
        # b_slice = ar[:i]
        # values of slice after i
        a_slice = ar[i+1:]
        # values of remaining slices
        rem_slice = a_slice
        for c in range(0,len(rem_slice)):
            # value at ar and value of rem_slice at c
            item = [ar[i], rem_slice[c]]
            # add to overall list of indicies
            indexlist.append(item)

    # set paircounter to zero
    paircounter=0
    # modulo pairs by k
    for each in indexlist:
        # sum of pairs
        # each[0] is i, each[1] is j
        pairsum = each[0]+each[1]
        # if i<j
        if each[0] < each[1]:
        # if divides easily by k
            if pairsum%k == 0:
                # then count as meeting criteria
                paircounter = paircounter+1

    return(paircounter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
