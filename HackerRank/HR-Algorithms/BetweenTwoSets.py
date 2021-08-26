# https://www.hackerrank.com/challenges/between-two-sets/problem

# There will be two arrays of integers.
# Determine all integers that satisfy the following two conditions:
# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array

# hint - use sets() to get uniques of a function
# hint - for all modulus == 0 (divided evenly), add a[x] to final count

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):

    new_a = []
    # create new a list
    for c in range(0,len(a)):
        a_before = a[:c]
        # print(a_before)
        a_after = a[1+c:]
        # print(a_after)
        a_remain = a_before+a_after
        # print('a_remain: ',a_remain)
        # we don't take the last self*self
        if a[c] < a[len(a)-1]:
            self = a[c]*a[c]
            # print(self)
            new_a.append(self)
        # print(new_a)
        for elem in a_remain:
            # print('append elem*a[c]: ',elem*a[c])
            new_a.append(elem*a[c])

    # finalize by combining new_a with original_a
    # print('combining new_a and a')
    new_a = new_a+a
    # insert the list to the set
    a_set = set(new_a)
    # convert the set to the list
    a_unique_list = (list(a_set))
    # print(a_unique_list)
    # print('sorting a_unique_list...')
    a_unique_list = sorted(a_unique_list)
    # print(a_unique_list)

    # now that we have a_unique_list, we can go through and divide each element
    # for any element where the sum(modulus) == 0, we count it.

    # we start off assuming all uniques are valid
    validuniques = len(a_unique_list)
    # print('Currently we think all uniques are valid, total of: ',validuniques)

    for unique in a_unique_list:
        # print('now checking...',unique)
        for i in range(0,len(b)):
            # print('checking against...',b[i])
            if b[i]%unique != 0:
                # print('modulus is not 0, uneven.')
                # print('subtract from validuniques...')
                validuniques=validuniques-1
                # print('validuniques is now: ',validuniques)

    # print('final validuniques found is: ',validuniques)
    return(validuniques)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
