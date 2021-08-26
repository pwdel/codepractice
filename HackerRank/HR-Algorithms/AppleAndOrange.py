# https://www.hackerrank.com/challenges/apple-and-orange/problem

# hint - you really have to understand what you are doing in terms of setting coordinates.
# if you define the apple tree as zero, everything else must be scaled by, "a", the apple tree.
# this includes both the positions of the static items - the orange tree, the house sides
# but it also includes each position of each apple or orange hit
# s,t is inclusive, so it must use <= and >= not just < or >

# hint - think about what the logical, "or" and "and" mean in terms of "real life."
# or means, "on either side of something" whereas "and" means "in between two of something"
# or can be used exclusively by pointing outward or inclusively of all by pointing inward
# and can be used exclusively, excluding either the outward area or the inward are of two points

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # print('start house measurement: ',s)
    # print('end house measurement: ',t)
    # print('apple tree location: ',a)
    # print('orange tree location: ',b)
    # print('apples thrown: ',apples)
    # print('oranges thrown: ',oranges)

    # print('set numberline to equal zero at a...')

    # print('setting apple tree to zero.')
    appletree=a-a
    # print('appletree coordinate: ',appletree)
    # print('setting houseleft to s-a')
    houseleft=s-a
    # print('houseleft coordinate: ',houseleft)
    # print('setting houseright to t-a')
    houseright=t-a
    # print('houseright coordinate: ',houseright)
    # print('setting orangetree to s-a')
    orangetree=b-a
    # print('orangetree coordinate: ',orangetree)
    # print('houseleft: ',houseleft)
    # print('houseright: ',houseright)
    # print('houselength: ',houseright-houseleft)

    hitapples=0
    # print('eliminate all apple values where d<houseleft and d>houseright')
    for each in range(0,len(apples)):
        applecoord=apples[each]+appletree
        # print('applecoord: ',applecoord)
        # if applecoord lands above or at left
        if applecoord >= houseleft and applecoord <= houseright:
            # print('appledistance thrownout is: ',each)
            # print('apple hit!')
            hitapples=hitapples+1
            # print('apple coordinate: ',applecoord)
            # print('apples hit so far: ',hitapples)

    hitoranges=0
    for each in range(0,len(oranges)):
        # print('----------')
        orangecoord=oranges[each]+orangetree
        # print('orangecoord: ',orangecoord)
        if (orangecoord) <= houseright and (orangecoord) >= houseleft:
            # print('orange hit!')
            # print('orange distance thrownout is: ',each)
            hitoranges=hitoranges+1
            # print('orange coordinate: ',orangecoord)
            # print('oranges hit so far: ',hitoranges)

    # print('Counting the values in each list...total is: ',totalcount)
    # totalcount = len(apples)+len(oranges)

    print(hitapples)
    print(hitoranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
