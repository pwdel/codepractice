# https://www.hackerrank.com/challenges/exceptions/problem

# note that exceptions can be either customized or print out a standard error message, contained in the error type.
# you don't have to go with the standard error type, you can print a custom message with more or less information.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# we first have to read from STDIN, then put into a list
if __name__ == '__main__':
    N = int(input())
    # print(N)
    # first, take all of the stdin input and put into a readable string
    allstring = '\n'.join([input() for _ in range(N)])

    # next, split the string line by line based upon each newline \n
    stringlist = allstring.split('\n')

    # for the range of N, integer inputs
    for i in range(0,N):
        # print("i is equal to: ",i) # <-- uncomment to check current i
        # grab the current line command from the indexed list
        commandline = stringlist[i]
        # values appear to be seperated and found at place 0 and 2
        # space seperator in between at 1
        # print(commandline[0],'and',commandline[2]) <-- uncomment to inspect commandline

        try:
            print(round(int(commandline[0])/int(commandline[2])))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except  ValueError as e:
            print("Error Code:",e)
