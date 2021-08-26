# Enter your code here. Read input from STDIN. Print output to STDOUT

# splits input into a list
N = input().split()

# grab the first item in the list as x
x = int(N[0])

# eval(expression, globals=None, locals=None)
# eval function runs the python code (which is passed as an argument) within the program.
# eval(expression, globals=None, locals=None)
# so eval(input() == int(N[1])) is asking to evaluate whether input() == int(N[1])
# then print prints out true/false
print(eval(input()) == int(N[1]))
