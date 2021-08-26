# https://www.hackerrank.com/challenges/zipped/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

# collections https://docs.python.org/3.8/library/collections.html#collections.Counter
# A Counter is a dict subclass for counting hashable objects. It is a collection where
# elements are stored as dictionary keys and their counts are stored as dictionary values.

# The zip() function takes iterables
# (can be zero or more), aggregates them in a tuple, and return it.
# zip(*iterables)

# how zip works, basically
# >>> nolist=[1,2,3]
# >>> stlist=['one','two','three']
# >>> result=zip()
# >>> result_list=list(result)
# >>> result = zip(nolist,stlist)
# >>> result
# <zip object at 0x109d0d480>
# >>> result_set = set(result)
# >>> result_set
# {(3, 'three'), (2, 'two'), (1, 'one')}

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    # strip() removes leading and trailing characters, cleans it up
    # list puts the arguments into a list
    N = list(input().strip())

    # grab the third argument in the first line, which shows the # following lines
    num_subjects = int(N[2])

    # students
    num_students = int(N[0])

    # create a range list specified by range(num_students) to represent students
    # this should work dynamically according to total num_students
    range_students = lambda a : [y for y in range(num_students)]
    # create the actual student list
    student_list = range_students(num_students)

    # iterate through next lines of subjects
    for i in range(0,num_subjects):
        # put split (cleaned) inputs, map them to a float
        # put them into a list
        # set to (map) to float, one decimal place
        a = list(map(float, input().split()))
        # a now contains a list for the one line in question
        print(a)

    # place to store result, empty result
    result=zip()
    # result_list
    result_list=list(result)
    # actual result
    result = zip(nolist,stlist)
