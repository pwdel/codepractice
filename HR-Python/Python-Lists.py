# https://www.hackerrank.com/challenges/python-lists/problem

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# import all necessary libraries
import re

if __name__ == '__main__':
    N = int(input())
    # print(N)
    # first, take all of the stdin input and put into a readable string
    allstring = '\n'.join([input() for _ in range(N)])

# the string of the entire output is now called, "allstring" and is line-by-line.
# in order to remove the following line, we have to partition the string
# allstring.partition('\n')[i]

# once we have read all inputs to a string, we can split the string line by line
# and more importantly, we can split it line by line into an indexed list.
stringlist = allstring.split('\n')

# set an overall list to store things, empty to start off with
overalllist=[]

# then we can go through a for loop to read the string line by line
# we start at line 0, and go through the N to extract command lines from ALL lines
# then for each command we need an if function for each command type
for i in range(0,N):
    # print("i is equal to: ",i) # <-- uncomment to check current i
    # grab the current line command from the indexed list
    commandline = stringlist[i]
    # extract the exact command as a list of 1 to 3 elements from the command line
    # this also includes blank elements as ''
    command = re.findall(r'\w{,}',commandline)
    # clean blank elements from command list
    command = list(filter(None, command))

    # print(command) # <-- uncomment to se command
    # split the command into a number and a command
    # argument
    # use a regex, or'ing each possible command to extract the argument
    # we have to make sure there is actually a value to parse
    if command != None:
        # arg always exists at 0
        commandarg = command[0]
        # if commandlist has 2 elements
        if len(command) == 2:
            # the second item [1] is automatically the val
            # convert to int from string!
            commandval = int(command[1])
        # if the commandlist has 3 elements
        elif len(command) == 3:
            # the last item [2] is automatically the val and [1] is pos
            # convert to ints from strings!
            commandpos = int(command[1])
            commandval = int(command[2])
    # otherwise, if no command set commandarg to None pass.
    else:
        # print("i is equal to: ",i)
        commandarg = None

    # now with the assumption that all commandargs will only
    # access the elements of the commandlist above needed
    # exactly according to the commandargs that they are
    # then we can use an if statement for each command statement, properly written
    # to modify our overall list

    # if function for if empty
    if commandarg == None:
        # do nothing
        pass
    elif commandarg == 'insert':
        # insert Insert integer at position insert(index,value)
        # using commandpos and commandval
        # we only have three elements for command 'insert'
        overalllist.insert(commandpos,commandval)
        pass
    elif commandarg == 'print':
        # print - Print the list.
        # we only have one element for command 'print'
        print(overalllist)
        pass
    elif commandarg == 'remove':
        # Delete the first occurrence of integer
        # we only have two elements for command 'remove'
        overalllist.remove(commandval)
        pass
    elif commandarg == 'append':
        # Insert integer at the end of the list.
        # we only have two elements for command 'append'
        overalllist.append(commandval)
        pass
    elif commandarg == 'sort':
        # sort the list
        # we only have one element for command 'sort'
        overalllist = sorted(overalllist)
        pass
    elif commandarg == 'pop':
        # pop the last element out
        # we only have one element for command 'pop'
        overalllist.pop()
        pass
    elif commandarg == 'reverse':
        # reverse the list
        # we only have one element for command 'reverse'
        overalllist.reverse()
        pass
