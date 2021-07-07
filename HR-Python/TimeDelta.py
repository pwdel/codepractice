# https://www.hackerrank.com/challenges/python-time-delta/problem

# stdin example
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

#!/bin/python3

import math
import os
import random
import re
import sys
import time
import datetime as dt

# fmt = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#    print(int(abs((dt.strptime(input(), fmt) -
#                   dt.strptime(input(), fmt)).total_seconds())))

# Complete the time_delta function below.
def time_delta(t1, t2):
    # convert t1 and t2 to postfix time
    # format https://docs.python.org/3/library/datetime.html
    # Fri 01 May 2015 13:54:36 -0000
    # datetime.datetime(2012,4,1,0,0).timestamp()
    # t1p = time.mktime(datetime.datetime.strptime(t1, "%d/%m/%Y").timetuple())
    datetime.datetime(2012,4,1,0,0).timestamp()

    diff = t1p-t2p

    return(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
