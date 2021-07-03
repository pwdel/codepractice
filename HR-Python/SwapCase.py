def swap_case(s):
    # input HackerRank.com presents "Pythonist 2".
    # expected output hACKERrANK.COM PRESENTS "pYTHONIST 2".
    s = s.swapcase()
    return(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
