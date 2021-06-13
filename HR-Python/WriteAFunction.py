# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    # leap = False
    # Write your logic here

    # The year can be evenly divided by 4, is a leap year,
    if year%4 == 0:
        # print('Year can be evenly divided by 4')
        # unless the year can be evenly divided by 100, it is NOT a leap year
        if year%100 == 0:
            # print('Year can be evenly divided by 4 and 100')
            # unless the year is also evenly divisible by 400. Then it is a leap year.
            if year%400 == 0:
                # print('Year can be evenly divided by 4 and 100 and 400')
                leap=True
            else:
                # print('Year can be evenly divided by 4 and 100 but not 400')
                leap=False
        else:
            # print('Year can be evenly divided by 4 but not 100')
            leap=True
    # all other years false
    else:
        leap=False

    # print(year)

    return(leap)

year = int(input())
print(is_leap(year))
