# https://www.hackerrank.com/challenges/maximizing-xor/problem

# hint - the xor function works the same in both directions, directionality does not matter.
# hint - this is not needed but the bitshift, target =<< x, shifts the binary bits by x digits
# hint - you can convert decimal to binary with for example: bin(int(2))

# hint - the challenge is to be able to create a list of lists. The lists inside are pairs.
# XOR can only be used to XOR together two values at one time, because it's a logical function.
# so, you can set up a list of all pairs, for example: [[10,10],[10,11],[11,11]]
# by doing a for loop and creating a, "self pair" for the starting number.
# then, you can go in and create an inner for loop, matching that, starting number and all others
# you can index others using the slicing capability [:i] and [i+1:] to get all other numbers
# on either side of the starter number for that outer for loop.

# so with a nested for loop, you basically get all values.

# it is possible to accomplish this even computationally faster by using bit shifting.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    # changing l and r to left and right for readability
    left=l
    right=r
    # Iterate the input(lst) and calculate the permutation
    # create the testlist range of all elements to work on.
    testlist = [i for i in range(left,right+1)]
    # empty permutation list to hold all permutations
    permutationlist=[]
    selfflag=0
    for i in range(0,len(testlist)):
        # take the current element in testlist
        # Extract testlist[i] or m from the list.
        m = testlist[i]
        # print('we are now working on: ',m)

        permutationlist.append([m,m])
        # print('our starter permutationlist is: ',permutationlist)

        # remLst is remaining list
        # slicing from before [:1] and after [i+1:]
        remLst = testlist[:i] + testlist[i+1:]
        # print('adding the remlist: ',remLst)

        for c in range(0,len(remLst)):
            m_others = [m,remLst[c]]
            permutationlist.append(m_others)

    # print('sorting the permutationlist... ')
    sorted_permutationlist = sorted(permutationlist, key=lambda x: x[0])
    # print(sorted_permutationlist)

    # print('setting up xoreach list...')
    xoreachlist=[]
    for each in sorted_permutationlist:
        # print('xoring together our current values: ',each[0],' and ',each[1])
        xoredvalues = each[0]^each[1]
        # print('result is: ',xoredvalues)
        # print('adding to xoreachlist...')
        xoreachlist.append(xoredvalues)

    maxxoredvalue = max(xoreachlist)
    minxoredvalue = min(xoreachlist)

    # print('Our min and max xored values are: ',minxoredvalue,' and ',maxxoredvalue)

    return(maxxoredvalue)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
