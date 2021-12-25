# this is the built-in module for using regular expressions in python
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
"""
sentence = "Start a sentence and then bring it to an end"

# the compile method returns a pattern of regex that can be used to find matches. the returned object is a pattern of the compile method and not a string
# it is best practice to use raw strings in compiling patterns
# for creating patterns of MetaCharacters we need to escape them with a \
pattern = re.compile(r"abc")

# finditer method returns an iterator that contains all the matches of the pattern for given string
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

pattern = re.compile(r"coreyms\.com")

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
