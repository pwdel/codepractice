# https://www.hackerrank.com/challenges/2d-array/problem

# hint - the way that python lists access data is different than a coordinate system.
# where as with a matrix you would expect to access: (row,column) and though this works in pandas
# with lists you are accessing array[row][column], assuming it's organized in this manner.
# basically you just have to map out how to connect row and column for a particular array structure.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    arrlen=len(arr)
    arrhgt=len(arr[0])

    # print('the length of arr is: ', arrlen)
    # print('the height of arr is: ', arrhgt)
    # print('let the hourglass points be defined as the top left of the hourglass.')
    # print('this means our hourglass ending points are: x=',len(arr)-3-1,' y=',len(arr[0])-3-1)
    # print('thus the submatrix points are:')

    hourglasslen=3
    hourglasshgt=3
    indexsubmatrix=[]
    for ix in range(0,arrlen):
        # x point, add 1 to convert from index to geometry
        for iy in range(0,arrhgt):
            if (iy) <= arrhgt-hourglasshgt and (ix) <= arrlen-hourglasslen:
                # add each x point
                xpoint=[ix]
                # add each y point
                ypoint=[iy]
                bothpoints=xpoint+ypoint
                # print('the points we are adding are: ',bothpoints)
                # append y to x,y coordinate
                indexsubmatrix.append(xpoint+ypoint)

    # print('the number of hourglasses which fit into the overall matrix is: ',len(indexsubmatrix))
    # print('the overall submatrix index is:',indexsubmatrix)

    allhourglassmatrix=[]
    currenthourglassmatrix=[]
    hourglassshape = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
    # print('the hourglass shape is: ',hourglassshape)
    # now for each of the points identified in the submatrix, capture the values.

    for each in indexsubmatrix:
        # grab the matrix points
        xmtx=each[0]
        ymtx=each[1]
        # print('planned matrix point is: ',xmtx,ymtx)
        # construct the hourglass
        for point in hourglassshape:
            # extract the x,y points
            xhrgls = point[0]
            yhrgls = point[1]
            # print('planned value extraction point is: ',xhrgls+xmtx,yhrgls+ymtx)
            # map out value extraction points
            newextractedvalue = arr[xhrgls+xmtx][yhrgls+ymtx]
            # print('new extracted value is: ',newextractedvalue)
            # append to overall matrix
            currenthourglassmatrix.append(newextractedvalue)

        # once reached end of hourglass shape,
        # which is the same as moving to a new point in the indexsubmatrix
        # append and reset currenthourglassmatrix
        allhourglassmatrix.append(currenthourglassmatrix)
        # reset to blank
        currenthourglassmatrix=[]

    # print('the number of values in the final hourglass is: ',len(allhourglassmatrix))
    # print('the final hourglass matrix is: ',allhourglassmatrix)

    # print('now sum each hourglass matrix...')
    hourglasssums=[]
    for every in allhourglassmatrix:
        currentsum = sum(every)
        hourglasssums.append(currentsum)

    #print(hourglasssums)

    # print('and the maximum value is: ')

    maxvalue=max(hourglasssums)

    return(maxvalue)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
