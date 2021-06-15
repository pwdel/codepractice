# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    nestedlist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        combined = [name,score]
        nestedlist.append(combined)

    # sorted nested list
    sorted_grade = sorted(nestedlist, key=lambda x: x[1])

    # put into dictionary
    gradekeys = {}
    for i in range(0,len(sorted_grade)):
        # within each item in the nested list
        currentitem = sorted_grade[i]
        # grab the second interior list part [1], which is the grade
        # set that equal to the first interior list part [0], which is the name
        gradekeys[currentitem[0]] = currentitem[1]

    minimums = min(gradekeys, key=gradekeys.get)

    def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

    print(minimums)
