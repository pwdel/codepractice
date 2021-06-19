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

.
