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
