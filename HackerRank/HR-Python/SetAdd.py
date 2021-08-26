# Enter your code here. Read input from STDIN. Print output to STDOUT

# we first have to read from STDIN, then put into a list
if __name__ == '__main__':
    N = int(input())
    # print(N)
    # first, take all of the stdin input and put into a readable string
    allstring = '\n'.join([input() for _ in range(N)])
    # then, we put all items in the string into a list based upon newline
    # next, split the string line by line based upon each newline \n
    stringlist = allstring.split('\n')

    # then convert the list into a set
    stringset = set(stringlist)

    # finally convert set into an integer count
    countcountries = int(len(stringset))

    print(countcountries)
