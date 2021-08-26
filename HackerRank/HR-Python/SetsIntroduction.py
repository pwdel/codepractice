# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# note that sets are an unordered list with no duplicates.

def average(array):
    # your code goes here
    setofeach = set(array)

    average_each = sum(setofeach)/len(setofeach)

    # hackerank acts weird and does not return 3 decimal one liner.

    formatted = "{:.3f}".format(average_each)

    return(formatted)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
