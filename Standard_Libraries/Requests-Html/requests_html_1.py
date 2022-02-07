# pip install requests-html
# if you're parsing html it's better to use beautifuloup but for javascript requests-html is the way to go.

from requests_html import HTML

with open(r"./simple.html", "r") as html_file:
    source = html_file.read()

    # creating an html document ready for parsing
    # you have to pass the source as a keyword argument
    html = HTML(html=source)

# returns the full html document with it's tags
print(html.html)

# returns only the text in html and not the tags
# javascript section stays the same
print(html.text)

print()
print()

# retruns a list of tags the match the name and css_selector that is given.
# if first attribute is True only returns the first match
match = html.find("title", first=True)

# your match object has .text and .html attributes which return text and html-tag respectively.
# .tag attribute returns the name of the tag without any extra text.
print(match.html)
