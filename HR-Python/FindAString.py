# https://www.hackerrank.com/challenges/find-a-string/
# hint - the trick is that you can't write fixed code for individual characters in a string.
# e.g. you can't just go:  string[i]+string[i+1]+string[i+n]
# you have to slice the string, with string[i:(i+substringlen)]
# to be able to search of a substring of dynamic length


def count_substring(string, sub_string):
    # input ThIsisCoNfUsInG is output 1
    # input WoW!ItSCoOWoWW oW output 2
    # input AbBaAbBaAbBa Ab output 3
    # I am an Indian, by birth. Birth output 0
    # traverse through the string
    incidentcounter=0
    substringlen = len(sub_string)
    for i in range(0, len(string)-(substringlen-1)):
        # check if found pattern
        check = string[i:(i+substringlen)]
        # print(check)

        if check == sub_string:
            incidentcounter = incidentcounter+1

    return(incidentcounter)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
