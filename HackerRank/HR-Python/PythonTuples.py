
# a map function and map object:
# function - map() passes each item of the iterable to this function.

# Return double of n
# def addition(n):
#     return n + n

# We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))
# [2, 4, 6, 8]

# so basically, it applies the function to an array and returns an array
# you can turn a map object into a list by applying list()


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # convert to actual list
    integer_list_list = list(integer_list)

    # convert this to a tuple
    t = tuple(integer_list_list)

    # do the actual hash
    print(hash(t))
