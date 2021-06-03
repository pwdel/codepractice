# https://www.hackerrank.com/challenges/time-conversion/problem

# hint - midnight, 12:00:00AM Returns '00:00:00', not '24:00:00'
# there are two special cases - midnight and noon
# leading zero can be created with "{:02d}".format(digit)
# note you are asked to return a string, not print a string.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # input time is string 07:05:45PM
    # output time is string 19:05:45

    def ampmStrip(s):
        # we can get the last two strings by doing a negative index
        meridian = s[-2]+s[-1]
        return(meridian)

    meridian_inst = ampmStrip(s)

    def hmsExtract(s):
        # remove the last two characters, the meridian
        removed = s[:-2]
        # s is the standard time, split into h, m, s
        hours, minutes, seconds = removed.split(":")
        # convert to integers
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        return(hours,minutes,seconds)

    hours_inst,minutes_inst,seconds_inst = hmsExtract(s)

    def pushtoMilitary(hours,minutes,seconds,meridian):
        # is the setting AM or PM
        setting = meridian
        if setting == 'PM':
            if hours == 12:
                # noon special case at no hours added
                milhours = hours + 0
            else:
                milhours = hours + 12
        elif setting == 'AM':
            if hours == 12:
                # midnight special case at 0
                milhours = 0
            else:
                milhours = hours + 0
        # put leading 0's in front of each digit, convert to string
        secondsstr = "{:02d}".format(seconds)
        minutesstr = "{:02d}".format(minutes)
        hoursstr = "{:02d}".format(milhours)

        # return the full string
        fullstring = hoursstr+":"+minutesstr+":"+secondsstr
        return(fullstring)

    # create final result string instance for print
    finalresult = pushtoMilitary(hours_inst,minutes_inst,seconds_inst,meridian_inst)

    return(finalresult)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
