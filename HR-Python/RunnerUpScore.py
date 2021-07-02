# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# first we have to read input from stdin

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sorted_list = sorted(list(arr))

# the trick in finding the, "second largest" or nth largest in an array
# is to basically treat each element as though you are looking through a deck of numbered cards
# as you go through the deck, have a temporary largest and temporary second largest
# they can start out as the first two cards, regardless of the order of the pack
# starting at the third card (index 2) you go through and compare, keep replacing
# the first and second largest cards as you go along until you get through the whole deck.

maxitem = max(sorted_list)
tempsecond=sorted_list[0]
tempmax=sorted_list[1]
# Start from second last
# element as the largest
# element is at last
# range(start,end,step/direction)
for i in range(2,len(sorted_list)):
    if sorted_list[i] < tempmax:
        # print("sorted_list < tempmax")
        tempsecond = sorted_list[i]
        # print("tempsecond is now: ",tempsecond)
    elif sorted_list[i] > tempmax and sorted_list[i] != tempmax:
        # print("sorted_list > tempmax")
        tempmax = sorted_list[i]
        # print("tempmax is now: ",tempmax)
        tempsecond = sorted_list[i-1]
        # print("tempsecond is now: ",tempsecond)

second = tempsecond

print(second)
