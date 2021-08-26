# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    # import the regex library
    import re

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
        # print(commandline) # <-- uncomment to see each line
        try:
            # try compiling
            reg = re.compile(commandline)
            ans = True
        except re.error:
            # if there's a regex error
            ans = False
        # print true if no error
        print(ans)
