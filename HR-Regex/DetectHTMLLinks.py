# https://www.hackerrank.com/challenges/detect-html-links/problem

# we're tasked with stripping the following:

# listing all the links and the text name of the links.

# <p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
# <div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

# Expected output:

# http://www.quackit.com/html/tutorial/html_links.cfm,Example Link
# http://www.quackit.com/html/examples/html_links_examples.cfm,More Link Examples...




# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

# grab the input, turn it into an integer n
# anything not an integer will pass through and not be assigned to n
n = int(input())

# join as a string, each dictionary item on a new line
# [input() for _ in range(n)]
# list comprehension, for _ in range(n)
# _ gets thrown away, it's the same as using "each"
# range(n) alludes to the input n which gives us the number of lines to read from stdin.
# using list comprehension, which would be the same as doing:
# htmlpart = []
# for _ in range(n):
#   htmlpart.append(input())
htmlpart = '\n'.join([input() for _ in range(n)])

# html_links
# re.findall is a non-overlapping string pattern searching function.
# The string is scanned left-to-right, and matches are returned in the order found.
# return all matches, as a list of tuples if the pattern has more than one group
# results are placed into a dictionary of tupples [(A,B)(A,B)]
# A is the URL
# B is the title
parsed_urls = re.findall(r'(?<=<a href)="(.+?)".*?>(.*?)</a>', htmlpart)
# in the above regex,.
# uses positive lookbehind (?<=...)
# to identify <a href at previous to the http tag
# for...  ="(.+?)"
# "(.+?)" signifies one or more title characters of any type between double quotes ""
# .* Matches 0 or more repetitions of the preceding RE, "." meaning any character
# .*?>
# ? by itself instructs to match 0 or 1 repetitions of the preceding RE
# Adding ? after the qualifier makes it perform the match in non-greedy manner.
# as few characters as possible will be matched.
# for example <.*?> will match only '<a>'. so .*?> will only match >
# this is for anything following "(.+?)" so basically, "filter out > after the url"
# finally (.*?)</a> leverages </a> as a border condition

for html_link in parsed_urls:
    # for everything within
    # re.sub
    # re.sub(pattern, repl, string, count=0, flags=0)
    # Return the string obtained by replacing the leftmost non-overlapping
    # occurrences of pattern in string by the replacement repl.
    text = re.sub(r'<.*?>', '', html_link[1])
    # in the above, <.*?> is taking from [1] which is the second element in the dict
    # for the particular item in the list we are working on.
    # the second item is the title, so it's taking anything between <>
    # this is just to clean up the string according to the required ouput
    print(f'{html_link[0]},{text.strip()}')
    # f'' is a literal string, a string formatting mechanism like str()
    # {html_link[0]} is just the URL in a dict
    # whereas .strip() takes off any spaces on either side of our title
    # hence we end up with url, title
