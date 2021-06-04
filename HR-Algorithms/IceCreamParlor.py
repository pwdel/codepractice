# https://www.hackerrank.com/challenges/icecream-parlor/problem

# hint
# starter input (STDIN) is stated as follows:
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3

# note - a printed stepwise explination can be found at, "IceCreamParlor_Hint"

# create an empty dictionary object with:
# test = dict()
# https://docs.python.org/3/library/stdtypes.html#dict
# this is a mapping type, key-value pair

# we use the dictionary to track prices and steps/trips.
# we then return, in a sorted manner, the finalized dictionary output, sorted by steps/trips

# sorted(iterable,key)
# https://docs.python.org/3/library/functions.html#sorted
# returns a new sorted list from items in iterable
# key specifies a function of one argument used to extract a comparison key

# hint - to understand how the input/output works, you have to look at the bottom code.

# m = int(input().strip()) --- m is stripped from the input as an int.
# arr = list(map(int, input().rstrip().split())) --- arr is stripped and split and mapped.
# result = icecreamParlor(m, arr) --- the result is the function called
# then, fptr.write, writes the output of the returned function to STDOUT
# fptr.write(' '.join(map(str, result)))
# along with a new line
# fptr.write('\n')


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    # create an empty dictionary object
    test = dict()
    # for the entire length of arr
    for flavor in range(len(arr)):
        # if the flavor is not in the dictionary yet
        # basically if we haven't iterated over this value yet
        # put it in our dictionary as follows...
        if arr[flavor] not in test:
            # look at amount of money m
            # create a key at (money - flavorprice), the price difference
            # with a value at flavor+1, the non-ordinal index of that flavorprice
            # e.g., [1,2,3,4] rather than [0,1,2,3]
            # dictionary key added is the money we have, minus the price at this flavor.
            # basically we're keeping track of how much we hypothetically would have spent down with two values.
            # the value is the actual non-ordinal step or trip we are on before we reach zero.
            # we add (+1) to our index to get the value, because that gives us a number of trips rather than ordinal.
            # the dictionary gets replaced on the last go-around until just before the key is equal to zero.
            # so if we check
            test[m-arr[flavor]] = flavor+1
        else:
            # if the price difference has already been added to the dictionary, we're at the end.
            # this is because, using this price *difference* will hypothetically spend us down to zero when combined with our previous step
            # so, we return a sorted list, sorted by the first value
            # the sorted([iterable_list]), first item is basically the main flavor we were on that we were sorting through.
            # the sorting for that iterable, is the dictionary value, which is the price difference for the ordinate
            # since it's the ordinate, that means it was the last step/trip, not the current step/trip
            # in short....
            # so we're displaying: [flavor_step, dictionary_value_at_previous_(previous_flavor_step_found)]
            return sorted([flavor+1, test[arr[flavor]]])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
