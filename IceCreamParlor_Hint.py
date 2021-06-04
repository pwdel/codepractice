m=4
arr=[1, 3, 4, 6, 7, 9]

def icecreamParlor(m, arr):
    # Write your code here
    # create an empty dictionary object
    test = dict()
    # for the entire length of arr
    print('the len of arr is: ',len(arr))
    print('the range(len(arr)) is: ',range(len(arr)))
    for flavor in range(len(arr)):
        print('----------')
        print('now checking index: ',flavor)
        # if the flavor is not in the dictionary yet
        # basically if we haven't iterated over this value yet
        # put it in our dictionary as follows...
        if arr[flavor] not in test:
            print('found arr[flavor] price not in dictionary, it is:',arr[flavor])
            # dollar match amount is key, 1 based index is value
            # look at amount of money m
            # create a key at (money - flavorprice), the price difference
            # with a value at flavor+1, the non-ordinal index of that flavorprice
            # e.g., [1,2,3,4] rather than [0,1,2,3]
            print('Dictionary key added is:',m-arr[flavor])
            print('...this is the money we started with minus the price.')
            print('...our remaining money is now: ',m-arr[flavor])
            print('so dictionary key is a price.')
            print('Dictionary value added is:',flavor+1)
            print('this is the trip we are on, the non-ordinal index')
            test[m-arr[flavor]] = flavor+1
        else:
            print('found arr[flavor] in dictionary, it is:',arr[flavor])
            # if it has already been added to the dictionary, we're at the end.
            # sort by the non-ordinal index key, flavor+1
            print('Now, return a sorted list from items in an iterable, given a key.')
            print('The iterable is the following (flavor+1):',flavor+1)
            print('This is effectively the number of "trips" taken to spend all of the money.')
            print('...this is because, the number of trips is the number of times we had to add things to the dictionary.')
            print('flavor+1 is the index we are on, +1, or the non-ordinal step we are on.')
            print('The key is: ',test[arr[flavor]])
            print('This is the dictionary key, the list of prices.')
            print('...the dictionary value found at the price:',arr[flavor])
            print('we are sorting based upon the price at which we stopped our first scan, meaning the step/flavor we were scanning at.')
            print('the dictionary value at that key would be the price, but we are reporting the step not the price.')
            return sorted([flavor+1, test[arr[flavor]]])
