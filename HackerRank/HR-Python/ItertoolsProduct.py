# https://www.hackerrank.com/challenges/itertools-product/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
# need to view documentation on itertools
# https://docs.python.org/3/library/itertools.html#itertools.product


# we first have to read from STDIN, then put into a list
if __name__ == '__main__':

    # .split takes input and maps into a list
    # map applies a function to a list of values with map(function,value)
    # so list() creates a list
    # put it together and you have a split of the input, clean each value into an int
    # then put back into a list
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # then we use the itertool function *product
    # which computes the cartesian product and outputs a tuple.
    # https://docs.python.org/3/library/itertools.html#itertools.product

    print(*product(a, b))
