# https://www.hackerrank.com/challenges/itertools-permutations/problem

# https://docs.python.org/3/library/itertools.html#itertools.permutations

# You are given a string S .
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# first, read the stdin

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

# import permutations per the assignment
from itertools import permutations
import re

# grab the input into a variable
N = input()

# if we do print(N), then we get:
# HACK 2
# which is one line. So, we could turn this line into a readable format
# with no line seperation.
# one of the constraints is supposed to be that
# "The string contains only UPPERCASE characters."
# however there is clearly a numerical in there as well. So, we could use a regex.


# Regex to clean out, filter out all capitol letters of arbitrary length
regex_exp = r'[A-Z]{,}'

# clean up input to capitol letters, extract object as a string
Nclean = re.search(regex_exp, N).group(0)

# However we also need to grab the number, as it is used to set group sizes
# using positive lookbehind, look for a digit(s) after a space.
regex_expnum = r'(?<=\s)[\d]+'

# grab this result as groupsize, converted to a usable integer
groupsize = int(re.search(regex_expnum, N).group(0))

# we can first split this string, Nclean into a tuple to get into alphabetical order
Ncleantuple = tuple(Nclean)

# sort tuple alphabetically
Ncleantuplesorted = sorted(Ncleantuple)

# from cleaned string, seperate into a list of characters
Ncleanlist = list(Ncleantuplesorted)
# this leads to a list: ['H', 'A', 'C', 'K']
# or if deriving from Ncleantuplesorted ['A','C','H','K']

# now per the permutations documentation, putting into a list
# use the groupsize rule attached above.
permutationslist = list(permutations(Ncleanlist,groupsize))
# this prints things into typles, [('H', 'A'), ('H', 'C'), ... ]
# whereas we would like line by line strings, for which we need a for loop
# we also need to compress the tuples into strings

# finally, per the specifications, everything must be printed
# in a lexicographic sorted order
# Our initial output is --> HA, HC, HK, AH
# We need to end up at --> AC, AH, AK, CA
# this sorting process could be done above, as a tuple.

for each in permutationslist:
    print(''.join(each))
