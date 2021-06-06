# https://www.hackerrank.com/challenges/maximizing-xor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    # Iterate the input(lst) and calculate the permutation
    # create the testlist range of all elements to work on.
    testlist = [i for i in range(l,r+1)]
    # empty permutation list to hold all permutations
    permutationlist=[]
    for i in range(0,len(testlist)):
        # take the current element in testlist
        # Extract testlist[i] or m from the list.
        m = testlist[i]

        # remLst is remaining list
        # slicing from before [:1] and after [i+1:]
        remLst = testlist[:i] + testlist[i+1:]

        # Generating all permutations where m is first element
        for p in range(0,len(remLst)):
            # create the permutation with all other units in list
            permutationlist.append(p)

    print(permutationlist)

    # xor results of each elements in permutation list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
