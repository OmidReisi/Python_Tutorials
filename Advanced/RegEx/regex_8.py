import re


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

pat
mat
cat
bat
"""
sentence = "Start a sentence and then bring it to an end"

# re.I (or re.IGNORECASE) flag finds matches regards less of them being lowercase or uppercase
pattern = re.compile(r"start", re.I)
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

# re.M or (re.MULTILINE) flag allows the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline)
pattern = re.compile(r"^Ha", re.M)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# more on flags and regular expressions
# https://docs.python.org/3/library/re.html