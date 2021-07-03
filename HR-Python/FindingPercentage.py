# https://www.hackerrank.com/challenges/finding-the-percentage/problem

# The provided code stub will read in a dictionary containing key/value pairs of
# name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


# strip the entire command line into a string which incudes student:grades key:values
# as well as the call to action on the last student for whose grades we are interested in

# do the calculations on the student asked for by extracting the last line as the key to look for
# then using that key, calculate the average and print
# average can be calculated by sum(gradeslist)/len(gradeslist)

if __name__ == '__main__':
    n = int(input())
    # student marks is a dictionary, start with empty
    student_marks = {}
    # within the range of n, which is our
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    for key, value in student_marks.items():
        if query_name == key:
            sum = 0
            count = 0
            for i in value:
                sum += i
                count += 1
            average = sum/count
            print("{:.2f}".format(average))
