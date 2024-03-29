# View the Google CoLab Notebook on this project:
# https://colab.research.google.com/drive/1ZZl6vgGWtDOE__WqthmAz1zuZkzh1hZ0?usp=sharing

# helpful tool:
# https://regexr.com/

# the dot
# https://www.regular-expressions.info/dot.html

print("(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.")

print("{m} Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, a{6} will match exactly six 'a' characters, but not five.")

print("\ Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; special sequences are discussed below.")

print("The special sequences consist of '\' and a character from the list below. If the ordinary character is not an ASCII digit or an ASCII letter, then the resulting RE will match the second character. For example, \$ matches the character '$'.")

print("SPECIAL SEQUENCES")

print("\ number Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, (.+) \1 matches 'the the' or '55 55', but not 'thethe' (note the space after the group). ")
print("\A Matches only at the start of the string.")
print("\b r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.")
print("\B is the opposite of \b, r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'")
print("\d Matches any Unicode decimal digit")
print("\D Matches any NOT decimal digit")
print("\s Matches any whitespace character")
print("\S Matches any NOT whitespace character")
print("\w Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore.")
print("\W Matches any NOT word Unicode word characters.")
print("\Z Matches the end of a string.")


# --- regex_pattern = r"^(.{3}\.){3}.{3}$"
# Do not delete 'r'.

print("^ Matches the start of the string")
print("() Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group")
print(". matches any character except a newline")
print("{m} Specifies that exactly m copies of the previous RE should be matched")
print("\ Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence")
print("The special sequences consist of \ and a character from the list above.")
print("^(.{3}\.) gives you: GROUP -> START 3 Copies of any character should be matched. DONE ")
print("^(.{3}\.){3} gives you: Do the proceeding command three times again.")
print("$ Matches the end of the string or just before the newline at the end of the string")
print("^(.{3}\.){3}.{3}$ gives you: Do the first command three times, twice - END OF STRING!")


# if input is 06-11-2015
# Your task is to match the pattern xxXxxXxxxx
# where x is a digit character and X is non-digit

# Regex_Pattern = r"(\d{2}\D){2}\d{4}"	# Do not delete 'r'.

# Alternate - r"^\d{2}\D\d{2}\D\d{4,}$" # Do not delete 'r'

print("^ starts string. \ allows special characters. d{2} two decimals")
print("$ ends string.")

# whitespace

# r"^(.{3}\.){3}.{3}$"
# r"^\d{2}\D\d{2}\D\d{4,}$"

# r"^\s{2}\S\s{2}\S\S{4,}$"

# sample input: 12 11 15


print("* Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.")
print("+ Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just 'a'")
print("*?, +?, ?? The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', it will match the entire string, and not just '<a>'. Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using the RE <.*?> will match only '<a>'")
print("|A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.")
print("(...) Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group")


# open ended matching at end of string

print("note the . denotes any character and the {,} denotes a wildcard for quantity.")

# Matching by group number

print("^[A-Za-z.\s_-]+$ allows uppercase or lowercase alphabetical characters, spaces, periods, underscores, and dashes only.")
"^ asserts that the regular expression must match at the beginning of the subject [] is a character class - any character that matches inside this expression is allowed A-Z allows a range of uppercase characters a-z allows a range of lowercase characters . matches a period rather than a range of characters \s matches whitespace (spaces and tabs) _ matches an underscore - matches a dash (hyphen) + asserts that the preceding expression (in our case, the character class) must match one or more times $ Finally, this asserts that we're now at the end of the subject"

print("[A-Za-z] matches uppercase and lowercase letters.")
print("Matching regex groups: you can match by group number by ensuring each expressing is surrounded by () and then referecning by number \1 \2 \3.")
print("The backreferences match EXACTLY what was captured by the referenced group, not the expression of the referenced group.")

# backreference to failed group, or group that matched nothing.

# what does this do...?
# ^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$
# ^ start string
# \d digit {2} twice
# () capture group of - character ? between 0 and 1 of those
# \d {2} 2 digits
# \1 repeat group 1, which is (-?)

# repeating expressions

print("Certain expressions might work differently in different environments.  For example:")
print("r'^[02468A-Za-z]{40}[13579\s]{5}$' # <-- did work in compiler, but not in Colab.")

# Matching {x, y} Repetitions

print("This pattern was solved immediately: Regex_Pattern = r'^\d{1,2}[A-Za-z]{3,}\W{0,3}$'")
print("Keep in mind that, {0,3} can represent a range of characters from 0 to n characters.")

# Multiple Repetitions

print("{0,} can be used to indicate, 0 or more.")
print("+ can be used to indicate, 1 or more.")
print("+ is equivalent to {1,}")

# Matching Ending Items

print("Used Regex_Pattern = r'^[A-Za-z]*s$' - the * helps match the last character. How?")
print("* Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.")
print("s$ shows that the last character will indeed be s ")

# Alternative Matching

print("the | can be used as an, 'or' expression.")
print("Regex_Pattern = r'^((Mr\.)|(Mrs\.)|(Ms\.)|(Dr\.)|(Er\.)){1}[a-zA-Z]+$'' # <-- does not work in Colab, but works in compiler.")
print("Why?")
print("The group (Mr\.) takes care of Mr. and each subsequent term in the overall group (A|B|C), alternating or statements.")
print("The \. character... Regular expressions use the backslash character (\) to indicate special forms or to allow special characters to be used without invoking their special meaning.")
print("So basically \ just allows you to literally capture the . character without . meaning, matching any character except newline.")

# Word Boundaries

print("Word boundaries seem to be able to be more powerful than ^ and $ as they can start at any arbitrary character.")
print("Notes: if the start point was a vowel, it's important to group: ([aeiouAEIOU])")
print(" further, [a-zA-Z\s]* as an optional, including the whitespace character helps obtain additional words.")

print("\b Matches the empty string, but only at the beginning or end of a word.")
print("A word is defined as a sequence of word characters.")
print("Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa)"t())
print("...or between \w and the beginning/end of the string.")

print("This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.")

# escapes in general:

# Most of the standard escapes supported by Python string literals are also accepted by the regular expression parser:

# \a      \b      \f      \n
# \N      \r      \t      \u
# \U      \v      \x      \\

# Capturing & Non-Capturing Groups

print("(?:) can be used to create a non-capturing group.")
print("Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.")
print("This seems to mean that we can reference the group by number with \1 and it will reference the expression rather than the exact substring.")

# backreferences

print("backreferences for regex can't be done in python")

# forward references

print("forward references for regex can't be done in python")

# positive lookahead

print("(?=...) Matches if ... matches next, but doesn’t consume any of the string. ")

print("The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2")

print("?= Matches if ... matches next, but doesn’t consume any of the string.")
print("For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.")
print("Just be careful about what you are looking to match and what is preceding, don't mix the two up!")

# negative lookahead

print("The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2.")

print("(?!...) ")
print("Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.")

# Positive Lookbehind

print("(?<=...) Matches if the current position in the string is preceded by a match for ... that ends at the current position.")
print("(?<=)")
print("The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2.")
print("(?<=...)")
print("Matches if the current position in the string is preceded by a match for ... that ends at the current position.")
print("this example looks for a word following abc by using ?<=abc ")
print(">>> m = re.search('(?<=abc)def', 'abcdef'")
print(">>> m.group(0)")
print(">>> 'def' ")
print("This example looks for a word following a hyphen:")
print(">>> m = re.search(r'(?<=-)\w+', 'spam-egg')")
print(">>> m.group(0)")
print(">>> 'egg'")

print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
# python regex documentation

print("re.findall(pattern, string, flags=0)")
print("Return all non-overlapping matches of pattern in string, as a list of strings.")
print("The string is scanned left-to-right, and matches are returned in the order found.")
print("If one or more groups are present in the pattern, return a list of groups; ")
print("this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result.")

print("--------------------------------------------------------------------------------")
re.search(pattern, string, flags=0)
Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
