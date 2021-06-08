# hint - while loop may be better than a for loop because ith as a natural exit after a defined result
# whereas a for loop needs to go through all 10000 results in order to print an answer, YES
# the while loop has a risk of being infinite (which can be mitigated) whereas a for loop is just more intensive.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # print('x1: ',x1)
    # print('v1: ',v1)
    # print('x2: ',x2)
    # print('v2: ',v2)

    samespotflag = 0
    counterflag = 0
    n=0
    while (samespotflag == 0) and (counterflag <= 10000):
        k1pos = x1+v1*n
        # print('first kang pos: ',k1pos)
        k2pos = x2+v2*n
        # print('first kang pos: ',k1pos)
        # print('Iterating n. n starting at: ',n)
        n=n+1
        # print('n is now: ',n)


        # print('Checking to see if k1pos and k2pos the same.')
        if k1pos == k2pos:
            # print('Setting samespotflag as true')
            samespotflag = 1
            return('YES')


        counterflag = counterflag+1
        # print('counterflag is now: ',counterflag)

        if counterflag == 10000:
            return('NO')




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
