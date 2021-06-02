# https://www.hackerrank.com/challenges/staircase/problem
# last line must have zero spaces
# requested to print not return
# hint - make sure to check inputs if you write code in a different notebook and change variable names for testing purposes

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    def repeater(n):
        holder=[]
        for level in range(0,n):
            levelspaces = ' '*(n-level-1)
            levelhashes = '#'*(level+1)
            levelall = levelspaces+levelhashes
            holder.append(levelall)
        # return the holder value
        # list of all levels
        return(holder)

    # create an instance of holder, list of levels
    holder_inst = repeater(n)

    # print out list in specified order
    def builderPrint(holder):
        for level in holder:
            print(level)

    builderPrint(holder_inst)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)



if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
