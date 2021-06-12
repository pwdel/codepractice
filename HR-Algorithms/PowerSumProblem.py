# https://www.hackerrank.com/challenges/the-power-sum/problem

# hint

# find the number of ways that int X,
# can be expressed as
# sum( (NaturalNumbers^Nth) )
# the sum of the Nth powers of unique, natural numbers
# X=13, N=2
# find 2^2+3^2 = 4+9=13

# function should return number of possible combinations
# 1<X<1000, 2<n<10

# In : X=10, N=2
# Expected Output = 1

# recursive functions have to have some way to, "bottom out" - some way of decreasing a variable
# or alternatively, there should be a finite input
# or, a recursive function is used to check the status of something on an ongoing basis

# hint - we can start out creating a recursive, "stop point," by stopping when Y^N > X because we have
# then passed all possible answers.

# Dynamic Programming Tutorials:
# https://www.youtube.com/watch?v=P8Xa2BitN3I
# https://www.youtube.com/watch?v=OQ5jsbhAv_M
# https://www.youtube.com/watch?v=ENyox7kNKeY
# https://www.youtube.com/watch?v=ocZMDMZwhCY
# https://www.youtube.com/watch?v=tp4_UXaVyx8

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    print(X)
    print(N)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
