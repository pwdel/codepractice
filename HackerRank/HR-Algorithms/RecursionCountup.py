y=100
def countup(y):
    print('y is starting out at: ',y)
    if y >= 1:
        print('we found that y >=1.')
        print('so y-1 is = ',y-1)
        print('we now call countup(y-1)')
        countup(y - 1)
        print('now after calling countup(y-1), y is: ',y)
        print(y)

    print('this is the end of the function.')

countup(y)
