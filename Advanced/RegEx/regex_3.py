import re

# the following are the regular expressions patterns
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# the following are anchors for patterns
# \b      - Word Boundary (Whitespace (space, tab, newline) before the pattern)
# \B      - Not a Word Boundary (NO Whitespace (space, tab, newline) before the pattern)
# ^       - Beginning of a String (only recognizes matches the are at the very beginning of the string)
# $       - End of a String (only recognizes matches the are at the very end of the string)

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
sentence = "Start a sentence and then bring it to an end"


pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

with open(r"./random_data.txt", "r") as f:
    content = f.read()

    matches = pattern.finditer(content)

    for match in matches:
        print(match)
