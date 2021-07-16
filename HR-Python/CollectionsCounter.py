# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

if __name__ == '__main__':
    # N = int(input())

    # print(N)

    # input is as follows, need to seperate it out line by line

    # 10
    # 2 3 4 5 6 8 7 6 5 18
    # 6
    # 6 55
    # 6 45
    # 6 55
    # 4 40
    # 18 60
    # 10 50

    # We get EOFError: EOF when reading a line, need to use try/except and print off error since its native to the IDE.

    # input convered to int, gives us number of lines
    # n = int(input())

    # split the input and map it
    # create a map object <map object at "whatever">
    # applies a function, iteratively over a list, tuple, etc.
    q = map(int,input().split())
    # print(q)

    # Counter is a construct from the collections library
    s = Counter(map(int,input().split()))
    # A counter is a container that stores elements as dictionary keys,
    # and the element counts are stored as dictionary values.
    # print(s)
    # the counter will look like:
    # Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})
    # this is derived from the original input:
    # 2 3 4 5 6 8 7 6 5 18
    # note we're getting a, "count" of how many times each value is present

    # input convered to int, gives us number of lines
    x = int(input())
    # list to hold totals
    total = []
    for i in range(x):
        # for the range of the input
        # split items which are in two's into a/b
        a,b = map(int,input().split())
        # if our counterobject[a] > 0
        # basically, if the requested number is present
        if s[a] > 0:
            # then append the total, b, which is given
            total.append(b)
            # use Counter subtract method
            # subtracts the counts of elements present in an iterable
            # object or a mapping object from the counter object.
            # basically removes the element
            s.subtract(Counter([a]))
        else:
            pass

    print (sum(total))
