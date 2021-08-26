# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Hint: output needs to be space seperated
# Print two space-separated long integers denoting the respective minimum and maximum values
# "space seperated" does not mean using ' ' - there must be a special space character
# output needs to be able to be larger than 32 bit - python runs at 64 bit by default
# looking at the main code at the bottom, "rstrip()" is used which strips off all of the whitespace
# after the characters.
# "split()" is used which splits the characters, so basically adding, ' ' is not needed.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    def listSorter(arr):
        # sort list from smallest to biggest
        arr.sort()
        # function above sorts variable itself, put in output variable
        sorted = arr
        return(sorted)

    # create instance of sorted list
    sorted_inst1=listSorter(arr)

    def minFinder(sorted_inst):
        # take the smallest items on the list
        mins = arr[0:(len(sorted_inst)-1)]
        # return the minimums
        return(mins)

    # create sorted instance
    mins_inst = minFinder(sorted_inst1)

    def maxFinder(sorted_inst):
        maxs = arr[1:len(sorted_inst)]
        return(maxs)

    maxs_inst = maxFinder(sorted_inst1)

    def valueSumPrinter(min,max):
        # sum of minimums
        minsum = sum(min)
        # sum of maximums
        maxsum = sum(max)
        # print it out with space seperation
        print(minsum,maxsum)

    sums_inst = valueSumPrinter(mins_inst,maxs_inst)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
