# https://www.hackerrank.com/challenges/coin-change/problem

# hint - You can solve this problem recursively but will not pass all the
# test cases without optimizing to eliminate the overlapping subproblems.

# Think of a way to store and reference previously computed solutions to avoid
# solving the same subproblem multiple times.

# hint - in the book, "Introduction to Algorithms," the Coin Change problem is referenced on page 446.
# this is part of chapter 16.

# Describe a greedy algorithm to make change consisting of quarters, dimes, nickels, and pennies. Prove that your algorithm yields an optimal solution.

# Suppose that the available coins are in the denominations that are powers of c, i.e., the denominations are c0;c1;:::;ck for some integers c > 1 and k   1. Show that the greedy algorithm always yields an optimal solution.

# Give a set of coin denominations for which the greedy algorithm does not yield an optimal solution. Your set should include a penny so that there is a solution for every value of n.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
