# https://www.hackerrank.com/challenges/any-or-all/problem

# https://docs.python.org/3/library/functions.html#any

# Return True if any element of the iterable is true. If the iterable is empty,
# return False. Equivalent to:

# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False

# https://docs.python.org/3/library/functions.html#all

# Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False

# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

# A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461) that remains the same when its digits are reversed.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

# invoke input to get number of items
N = int(input())

# invoke input again
# extract string of numbers into current
# split into list of items
current = input().split()

# map function to turn each item into int
# *map stops from returning map object but instead individual items
# so, do custom function instead
allints = list()
for i in range(len(current)):
    # turn each element into integer, append to list
    newint = int(current[i])
    allints.append(newint)

# rather than mess with lambda or map, keep predictable output
poslist = list()
for i in range(len(allints)):
    # check each element pos
    if allints[i] >= 0:
        poslist.append(True)
    else:
        poslist.append(False)

# use all to print whether all pos is true
# print(all(poslist)) # <-- uncomment to check
# store poscheck
poscheck = all(poslist)

# custom function predictable output for numerical palindrome
pallist = list()
for i in range(len(allints)):
    # convert each element to str
    strel = str(allints[i])
    # reverse element should use [::-1], -1 denotes backwards step
    if strel == strel[::-1]:
        pallist.append(True)
    else:
        pallist.append(False)

# use pallist to check if any true
palcheck = any(pallist)

if poscheck and palcheck == True:
    print(True)
else:
    print(False)
