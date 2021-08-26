# https://www.hackerrank.com/challenges/detect-html-tags/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    # grab the forcasted number of lines
    N = int(input())

    # create an empty list to hold strings
    stringlist = list()

    # run through and populate list
    for each in range(0,N):
        stringlist.append(input())

    # list to hold all found expressions
    foundexpressions=[]
    # do actual operations
    for i in range(0,len(stringlist)):
        # order and evaluate item by item
        currentitem = stringlist[i]
        # currentitem regex
        # <p>, <a>, <div>, (print out in alphabetical order)
        regex_epression = r'[<p]{,}.[<a]{,}'
        # search for item
        m = re.search(regex_epression, currentitem)
        # put group item into variable
        # prevent NoneType error with if statement
        if m is not None:
            # grab the group item, 0 since it's the only one
            groupitem = m.group(0)
        else:
            # otherwise empty
            groupitem = ""

        # need to do an if statement for only if object found
        # else, don't append. Can't add a nonetype object.
        if groupitem != None:
            # add group 0 to foundexpressions list
            foundexpressions.append(groupitem)

    print(foundexpressions)
