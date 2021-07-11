# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

print(N)

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

# first, take all of the stdin input and put into a readable string
splitbyline = '\n'.join([input() for _ in range(N)])

# next, split the string line by line based upon each newline \n
stringlist = splitbyline.split('\n')

# for the range of N, integer inputs
for i in range(0,N):
    # print("i is equal to: ",i) # <-- uncomment to check current i
    # grab the current line command from the indexed list
    commandline = stringlist[i]
