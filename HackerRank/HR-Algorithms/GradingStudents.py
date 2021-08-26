# https://www.hackerrank.com/challenges/grading/problem
# hint - the input is a series of lines, looks like it should be strings
# however if you debug through the hackerrank parser, you can see that it's a list.
# if you print the type(grades) then you see Debug output <class 'list'>
# therefore the original format given is list, not individual strings
# while the output format appears to be printed strings, it should be given as a list
# the below code strips the code and prints it out into strings

# hint - the modulo can be very useful, you have to really leverage this when figuring out
# logic of partial paths between numbers

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

# program logic
    # < 38 is failing
    # if (multiple5 - grade) < 3, round up
    # example if grade=7, then 10-7=3, if 3 < 3, do not round up
    # example if grade=8, then 10-8=2, if 2 < 3, round up

def gradingStudents(grades):
    # Write your code here
    # turn the input, which is lines of grades, into a list
    return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades]
    # logic explained...
    # iterate through the list
    # for i in grades

    # i if
    # return the grade itself

    # if (i < 38) or i%5 < 3
    # if less than 38, as discussed in instructions
    # or i modulo 5 is less than 3
    # basically do nothing if remainder is either 1 or 2, which works for both upper and lower half of each decade
    # keep in mind, the modulo is the remainder, it will always be less than the base being "modulo'd"

    # else i + (5 - i%5)
    # for all other cases, "else"
    # because i%5 < 3 covers the smaller-side numbers
    # otherwise (5 - i5) is basically 5-remainder, the amount left over
    # added to i gets you to the next "5"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
