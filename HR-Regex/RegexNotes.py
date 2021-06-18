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


# r"^(.{3}\.){3}.{3}$"
# Do not delete 'r'.

print("^ is")

print("() is ")

print(". is ")

print("{m} is ")

print("^(.{3}\ gives you...")
