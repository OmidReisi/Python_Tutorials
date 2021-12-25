import re

urls = """
some key websites
https://amazon.com
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# each group is indexed from 1
# group[0] is the whole pattern
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0))

# sub method takes a string and replaces the patterns in regex for the given text
# we can back-reference the groups in pattern by using  {\group number} to replace the patterns
subbed_urls = pattern.sub(r"https://www.\2\3", urls)
print(subbed_urls)
