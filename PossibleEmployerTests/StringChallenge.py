# For this challenge you will determine whether HTML elements are nested correctly.

# Have the function StringChallenge(str) read the str parameter
# being passed which will be a string of HTML DOM elements and
# plain text.
# The elements that will be used are: b, i, em, div, p.
# For example: if str is "<div><b><p>hello world</p></b></div>"
# then this string of DOM elements is nested correctly so your
# program should return the string true.

# If a string is not nested correctly,
# return the first element encountered where,
# if changed into a different element,
# would result in a properly formatted string.
# If the string is not formatted properly,
# then it will only be one element that needs to be changed.
# For example: if str is "<div><i>hello</i>world</b>"
# then your program should return the string div because
# if the first <div> element were changed into a <b>,
# the string would be properly formatted.

# Examples
# Input: "<div><div><b></b></div></p>"
# Output: div

# Input: "<div>abc</div><p><em><i>test test test</b></em></p>"
# Output: i

# == RUNNING TEST CASES ==
# == INPUT ==
# "<div>abc</div><p><em><i>test test test</b></em></p>"
# == OUTPUT ==
# <div>abc</div><p><em><i>test test test</b></em></p>
# << WRONG >>
# << EXPECTED OUTPUT: i >>
# == INPUT ==
# "<div><div><b></b></div></p>"
# == OUTPUT ==
# <div><div><b></b></div></p>
# << WRONG >>
# << EXPECTED OUTPUT: div >>


# Python version --------------
# 3.8.3 [GCC 8.3.0]
# Packages installed
# ------------------
# boto3
# numpy
# pandas
# requests
# scikit-learn
# scipy
# output logs will appear here


import re

def StringChallenge(strParam):

  # elements b, i, em, div, p

  # note - we could use beautifulsoup to do this much faster, but this is not noted as being, "installed"
  # so, we will use the native re to build a custom DOM element finder

  # wrong cases given as examples
  # 1. <p><em><i> -> </b></em></p>
  # : corrected...  <p><em><i> -> </i></em></p>
  # : expected output: i
  # : expects that we change the SECOND element from b to i
  # : starting element does not match closing element
  # : ASYMETRICAL solution 1,1,2,3,4,4,3,2
  # : plaintext given more than once
  # 2. <div><div><b></b></div></p>
  # corrected <div><div><b></b></div></div>
  # : expected output: div
  # : expects that we change the SECOND element from p to div
  # : starting element does not match closing element
  # : SYMETRICAL solution 1,1,2,2,1,1

  # psuedocode
  # 1. extract all of the tags into a list, e.g. div,div,b,b,div,p
  # 2. for each tag type, go through and count total into dict, e.g.
  # : {div: 3, b: 2, p: 1, i: 0, em: 0}
  # 3. it's directional, right to left, so for any odd numbers
  # : go right to left in the list [::-1] and find first
  #  instance of either odd1 or odd2 from the dict
  # 4. answer is the OPPOSITE of FIRST_INSTANCE found of odd1|odd2


  # extracting tags into a list
  # must use positive lookbehind, example:
  # regex_string = r'(?<=\<)[b]'
  # returns def in presence of b after <
  # might need to use escape character \ for <

  # there are multiple positive lookbehinds happening
  # syntax for multiple positive lookbehinds is grouping
  # we can also repeat grouping possibly with greedy search
  # greedy dot .*
  # but, greedy dot .* matches too much, it also matches <>
  # Adding ? after the qualifier makes it perform the match in minimal fashion
  # regex_string = r'(?<=\<)[b|i|em|div|p].*'

  # can we just replace - re.sub(pattern, repl, string)
  # regex_string = r'[a-zA-Z]' <-- would replace all /w
  # repetition + matches one or more of preceding
  # however if we use +/{,} it splits every character into spaces
  # we want to use .split() coming up so need to keep together

  regex_string1 = r'[\<]'

  removed_gt = re.sub(regex_string1, " ", strParam)

  # test out substitution, replaced < characters
  # print(m.group(0)) # <-- in case object
  # print(removed_gt)

  regex_string2 = r'[\>]'

  # use > to remove other end
  removed_lt = re.sub(regex_string2, " ", removed_gt)

  # test removed_lt
  # print(removed_lt) # <-- uncomment to test

  # split into a list - need to use for ordering later
  removedsymbolic_list = removed_lt.split()

  # slash regex
  regex_string3 = r'[\/]'

  # remove slash
  removed_slash = re.sub(regex_string3, " ", removed_lt)
  print(removed_slash)

  # for counting element purposes
  cleaned_list = removed_lt.split()

  # test symbolic list
  # print(removedsymbolic_list)

  elementdict = dict()
  elementdict = {'b':0, 'i':0, 'em':0, 'div':0, 'p':0}
  print(elementdict)
  # for each tag type, go through and count total into dict, e.g.
  for each in cleaned_list:
    if each == 'b':
      # elementdict["b"]=+1
      pass
    # print(elementdict)


  # code goes here
  return strParam

# keep this function call here
print(StringChallenge(input()))
