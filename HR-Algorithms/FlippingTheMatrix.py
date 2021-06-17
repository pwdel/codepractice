# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

# hint - a, "constructive algorithm" is building something mechanistic in the digital world.
# in this case, we're building a rubix cube.
# the problem statement is set up such that the code must operate to simulate how a rubix cube works.
# if you just assume you can rotate in any direction at all, the maximum of the top
# left quadrant would be the sum of all maximums.
# however, we are only able to assume that the columns can, "flip" while maintaining
# structure, which means that there is a grid shape that must maintain its shape
# basically certain cells can only ever go to other pre-destined points:

# A B B A
# C D D C
# C D D C
# A B B A

# in the above grid, A's can only take the place of other A's, B's with B's, etc.
# that's because this is how a rubix cube works in the physical world.
# therefore our absolute maximum can only be the sum of the maximums of any A, B, C, D group
# Otherwise, the sum of the maximum of all elements would be higher than the true result.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
