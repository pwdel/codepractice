# https://www.hackerrank.com/challenges/calendar-module/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

if __name__ == '__main__':
    N = input()

    # split into a list of date strings
    datelist = N.split(' ')

    # datelist 0 is month
    month = int(datelist[0])
    # datelist 1 is day
    day = int(datelist[1])
    # datelist 2 is year
    year = int(datelist[2])

    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    weekdaynumerical = calendar.weekday(year,month,day)

    # put into uppercase
    print(week_days[weekdaynumerical].upper())
