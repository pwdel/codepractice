# https://www.hackerrank.com/challenges/camelcase/problem

#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# sample input saveChangesInTheEditor

def camelcase(s):
    # Write your code here
    # list to store all upper or lower values
    casevector=[]
    for i in range(0,len(s)):
        # check if uppercase
        if s[i].isupper():
            casevector.append(1)
        else:
            casevector.append(0)

    return(sum(casevector)+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
