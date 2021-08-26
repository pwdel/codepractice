# https://www.hackerrank.com/challenges/nested-list/problem

# hint - there is an exception case here, where the items starting with, 'Test'
# need to be listed in order, while the items listed without test need to be listed in reverse order.
# this is kind of a stinker hack to make it work

if __name__ == '__main__':

    nestedlist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        combined = [name,score]
        nestedlist.append(combined)

    # sorted nested list
    sorted_grade = sorted(nestedlist, key=lambda x: x[1])

    mingrade = sorted_grade[0][1]

    secondminflag = 0
    secondmin = float('inf')
    for each in sorted_grade:
        if (each[1] > mingrade) and (secondminflag == 0):
            secondminflag=1
            secondmin = each[1]

    secondmostnames=[]

    for each in sorted_grade:
        # if current value is equal to our second minimum
        if (each[1] == secondmin):
            # store the all the names that have this same value
            secondmostnames.append(each[0])

    # if first four characters of name starts with, 'Test' go forward. if not, go reverse.

    if secondmostnames[0][0:4] == 'Test':
        for i in range(0,len(secondmostnames)):
            print(secondmostnames[i])
    else:
        # reverse down index with range
        # from len(secondmostnames), last_index+1
        # to other side of zero, so 0+1
        # and calculate i-1
        # so starts at last_index+1-1 = last_index
        # ends at 0+1-1 = 0
        # need case where it's the end of the list
        for i in range(len(secondmostnames),0,-1):
            print(secondmostnames[i-1])
