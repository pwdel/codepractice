if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    samplespace=[]
for a in range(0,x+1):
    # iterating through x
    # print('x is now: ',a)
    for b in range(0,y+1):
        # iterating through y
        # print('y is now: ',b)
        for c in range(0,z+1):
            # iterating through z
            # print('z is now: ',c)
            # add all permutations together
            zpermute=[a,b,c]
            # print('zpermute is now: ',zpermute)
            # add possible permutations to total list
            samplespace.append(zpermute)

# print(samplespace)

equalstore=[]
# go through and eliminate non-working items
for i in range(0,len(samplespace)):
    if sum(samplespace[i])==n:
        # store the index of the item that we need to remove
        equalstore.append(i)

# print('where to remove indexes: ')
# print(equalstore)

# moving backwards through list, remove each item in samplespace
length = len(equalstore)
i=length
while i > 0:
    # print('i is at: ',i)
    # remove the item at index shown in equalstore
    samplespace.pop(equalstore[i-1])
    # move down the index
    i=i-1

# print('samplespace with items removed: ')
print(samplespace)
