# https://www.hackerrank.com/challenges/strings-xor/problem

# basically, this is a debugging problem meaning there is only so many lines that can be changed.
# at first I approached this problem as though I'm re-writing the code to be more understandable.
# in reality, it just needs a quick fix.

# The actual debugging, once I understood that this is what the objective is - was much faster

# below I have put the debugged code as well as the incorrectly re-written code.

# hint - strings can be added to each other much like appending lists by doing:
# stringnew = stringnew + anotherstring

# hint - ; are not needed, this is not javascript
# hint - python uses == as the logical equal operator, as most languages seem to.


# note that you can only add or modify at most 3 lines of code!

### Correct Answer - Only Modified 3 Lines.

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res = res+ '0';
        else:
            res = res+ '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))






### Incorrect Answer - Rebuilt Everything.

s = input()
t = input()

def strings_xor(s, t):
    # print('function called! Executing strings_xor.')
    res = []
    for i in range(len(s)):
        if s[i] == t[i]:
            # print("i is now: ",i)
            res.append(0)
        else:
            res.append(1)

    resstr = ''.join([str(elem) for elem in res])
    return(resstr)

res = strings_xor(s,t)
# print('res is now: ',res)
print(res)
