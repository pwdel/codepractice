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
import datetime

# fmt = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#    print(int(abs((dt.strptime(input(), fmt) -
#                   dt.strptime(input(), fmt)).total_seconds())))

# Complete the time_delta function below.
def time_delta(t1, t2):
    # convert t1 and t2 to postfix time
    # format https://docs.python.org/3/library/datetime.html
    # Fri 01 May 2015 13:54:36 -0000

    # t1p = time.mktime(datetime.datetime.strptime(t1, "%d/%m/%Y").timetuple())
    fmt = '%a %d %b %Y %H:%M:%S %z'

    # print("t1p is: ",t1p)
    t1_p = datetime.datetime.strptime(t1, fmt)
    t2_p = datetime.datetime.strptime(t2, fmt)

    # format time difference in days, strip off days and multiply by seconds
    thedays = (t1_p - t2_p).days*24*3600
    # strip off seconds, same
    thesecs = (t1_p - t2_p).seconds

    # absolute value of both combined
    dayssecs = abs(thedays+thesecs)

    # turn into string
    dayssecsstr = str(dayssecs)

    return(dayssecsstr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
