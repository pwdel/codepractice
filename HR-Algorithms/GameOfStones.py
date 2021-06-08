# https://www.hackerrank.com/challenges/game-of-stones-1/problem

# hint - the input is a series of integers, not a list
# hint - if it's an even number of turns, B wins. If it's an odd number of turns A wins.
# hint - anything dealing with evens and odds can usually be found out with the modulo function.

# hint - this is ultimately an inductive problem, where the objective is to find an invariant
# the alternative would have been to find a lookup table with every possible decision tree and solve the entire game
# obviously that's not what the problem calls for, it's asking for a mathematical
# formula that can be turned into an if/else decision making statement with few parameters.

# hint - using modulo, you should look around the, "nearby parameters" to see if a pattern can be found.
# in this case, using the guidelines in the problem description, the following wins/losses are unchangable:
# for startpoints...
# 0->B, 1->B, 2->A, 3->A, 4->A, 5->A, 6->A, 7->B.
# working off of the assumption that A can force either 0 or 1 for the next turn on player B if it
# gets a number which can be reduced down to A having either [2,3,4,5,6] then we should look for
# a way to determine multiples of 2,3,4,5,6. The way to do this is to take n%7 and look at the remainder.
# if the remainder is either 2,3,4,5,6 this means the problem can be reduced down to A having 2,3,4,5,6
# which means that A can force 0 or 1 on B for the next turn, meaning A will win.

# hypothetically any modulo above 7 can be used in the same way, but you may need more if statements.
# this is the simplest if statement because it only requires the range of [2,3,4,5,6] and no other special
# remainders needed.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    # Write your code here
    if n%7 < 7 and n%7 > 1:
        winner = 'First'
    else:
        winner = 'Second'

    return(winner)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
