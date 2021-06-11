# https://www.hackerrank.com/challenges/coin-change/problem

# hint - You can solve this problem recursively but will not pass all the
# test cases without optimizing to eliminate the overlapping subproblems.

# Think of a way to store and reference previously computed solutions to avoid
# solving the same subproblem multiple times.

# Basically, if our objective is n = 1 and we have one coin, c=[1]
# the starting array of permutations is:  [1, 0]
# If we have two coins, and n=2, c=[1,2]
# the starting array of permutations is:  [1, 0, 0]
# with n=4 and c=[1,2]
# starting array of permutations is [1, 0, 0, 0, 0]
# basically the permutations represent the combinations that we could have.
# [1 ...] at the start represents the zero case.
# we go through each existing coin, [1,2]
# then, for that particular coin, in a range of coin [1] to n+1 (so 1+4 = 5), meaning from 1 to 4
# we iterate through and do:
# n_perms[i] = n_perms[i] + n_perms[i-coin]
# that is basically taking the previous value, which always starts out as 1 for the zero cases
# and adding it in at the current position, i, which is between the coin value [1] and the objective value [4]
# So what will happen is, you end up with [1,1,1,1,1]
# then, on the next round, the same thing happens, but you start at location, "2", so you get:
# [1,1,2,2] - and the maximum or last result is the final result.
# let's say you have 1 coins, [1,2,3]
# basically at each successive coin, the coin is going to signal to start adding in at our little, "notebook."
# so that will look like this:
# [1,1,1,1,1] -> [1,1,2,2,3] -> [1,1,2,3,4]
# basically, the "notebook" serves as a sort of rolling registry, with entry points at each coin value.
# So why does a rolling registry mathematically simulate the number of combination possibilities?
# The formula for possible permutations without repeating  where order matters is;
# permutations = n!/(n-r)! where n=objects, r=sample
# whereas 4! = 4*3*2*1, in this situation we're selecting only the available values under 4
# it is sort of like selective factorial: 4s! = 4*2*1 = 8, so 8/(4-2)! = 8/2 = 4
# Basically, adding an item to a registry at the end multiple times is the same as multiplying.
# in a sense, we're calculating that "selective factorial" at the end node of where we store the data.

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
    n_perms = [1]+[0]*n
    # print('the array of permutations is: ',n_perms)
    # print('this accounts for the zero case solution.')

    for coin in c:
        # print('----------     ----------     ----------')
        # print('n_perms is starting out as: ',n_perms)
        # print('We are now calculating for coin: ',coin)
        # print('Coin we are looking at is now of denomination: ',coin)
        # print('We are going to stop before: ',n+1,' because the iterations are counting up to the amount of times it takes to make that change amount.')
        for i in range(coin, n+1):
            # print('----------')
            # print('Index range is from our denomiation: ',coin,'to the change we are looking to make + 1: ',n+1)
            # print('We are now at index: ',i)
            # print('i-coin is: ',i-coin)
            # print('n_perms[i-coin] is: ',n_perms[i-coin])
            # print('while n_perms[i] where i=',i,' is currently ',n_perms[i])
            # print('adding n_perms[i-coin], which is: ',n_perms[i-coin],' to n_perms[i] which is: ',n_perms[i])
            n_perms[i] = n_perms[i] + n_perms[i-coin]
            #print('n_perms[i] is now...',n_perms[i])
            # print('The full n_perms array is: ',n_perms)

    return(n_perms[n])
