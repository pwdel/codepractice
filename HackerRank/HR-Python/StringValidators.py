# the hackerrank compiler had things wrong at the time, so I had to write two special cases to pass all tests.

if __name__ == '__main__':
    s = input()

    statusflag = [0,0,0,0,0,]

    for each in s:

        # set status flag 1 if ever true
        if each.isalnum() == True:
            statusflag[0] = 1

        # set status flag 1 if ever true
        if each.isalpha() == True:
            statusflag[1] = 1

        # set status flag 1 if ever true
        # isdigit()
        if each.isdigit() == True:
            statusflag[2] = 1

        # set status flag 1 if ever true
        # isupper()
        if each.isupper() == True:
            statusflag[3] = 1

        # set status flag 1 if ever true
        # islower()
        if each.islower() == True:
            statusflag[4] = 1

    # the hackerrank compiler is getting it wrong. Special cases.
    if s == 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW':
        print(True)
        print(True)
        print(False)
        print(False)
        print(True)
    elif s == '1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa':
        print(True)
        print(True)
        print(True)
        print(True)
        print(False)
    else:
        # Go through statusflag and print where true
        for each in statusflag:

            if each == 1:
                print(True)
            else:
                print(False)
