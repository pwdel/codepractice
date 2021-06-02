# https://www.hackerrank.com/challenges/diagonal-difference/problem

# hint - python arrays (non-pandas or numpy) are a list of lists
# hint - the array may not actually be square, they try to trick you into thinking it's always square!

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  # Write your code here
  # normalize matrix down to smaller dimension
  def regularize(arr):
    category='NoCat'
    bigdim='unknown'
    # if y and x dim same
    if len(arr) == len(arr[0]):
      # do nothing
      category='nochange'
      bigdim='same'
      arr=arr
      # if y dim larger than x dim
    elif len(arr) > len(arr[0]):
      category='ybigger'
      bigdim=len(arr)
      # slice the bottom y dim off
      # slice off by smaller dimension, len(arr[0])
      arr = arr[0:len(arr[0])]
      # if y dim smaller than x dim
    elif len(arr) < len(arr[0]):
      category='xbigger'
      newarr=[]
      # the larger dimension
      bigdim=len(arr[0])
      # columns first, all columns
      for ydim in range(0,len(arr)):
        # append each row, skipping the last column of each row
        # len(arr is the smaller dimension)
        newarr.append(arr[ydim][0:len(arr)])
        # return the newly crafted array
        arr=newarr

    # return
    return(arr,category,bigdim)


    # newly created arr, snipped off for length
    regarr,category,bigdim = regularize(arr)
    print(category)

    # set up empty lists
    def diagmaker(arr):
      righttoleftarr=[]
      lefttorightarr=[]
      for each in range(0,len(arr)):
        index.append(each)
        # start at n,0 and go to 0,n
        # get the rightleft point value
        rlpoint = arr[len(arr)-each-1][each]
        # append to the diag
        righttoleftarr.append(rlpoint)
        # start at 0,0 and go to n,0
        # get the leftright current point value
        lrpoint = arr[each][each]
        # append the point to the diag
        lefttorightarr.append(lrpoint)
        # return both diag's
      return(righttoleftarr,lefttorightarr)

    # create the actual diag's
    righttoleftarr,lefttorightarr = diagmaker(regarr)

    # sum of righttoleftarr
    rightsum = sum(righttoleftarr)
    # sum of lefttorightarr
    leftsum = sum(lefttorightarr)

    # absolute diagdiff
    absdiagdiff = abs(leftsum-rightsum)

    # return main function
    # absdiagdiff,leftsum,rightsum,righttoleftarr,lefttorightarr
    return(category,bigdim)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
