# beautifulsoup module alllows us to parse html content and get the results that we need
# you need a parser to use with this module and the built-in parser is html which is okey
# there are two external parsers called lxml and html5lib as well
# we use lxml that supports XML and html as well and it's faster than the other two parsers
# pip install beautifulsoup4
# pip install lxml
from bs4 import BeautifulSoup


with open(r"./Html/html_1.html", mode="r") as html_file:
    # to make your object pass a string of html or an html file and then the parser you want to use
    soup = BeautifulSoup(html_file, "lxml")

# this is a BeautifulSoup object that returns the html
# this prints html text as unicode(all lines are pushed to left)
# print(soup)
# print()

# this method keeps the html indentattion
# print(soup.prettify())

# the easiest way to access a tag is using it as an attribute of our beautifuloup object
# this way always returns the first tag it hits(if there are multiple tags of same kind then this way is no good)
match = soup.title
print(match)


# to remove the opening and closing tags we have to access the text attribute of our tag
print(match.text)


# this method returns a tage with the given specifics
# if there are multiple tags with the same specifics then it returns the first one
# first argument is the tag you want and then you can add more arguments to search for a specific tag
# the reason we use class_ is because class is a special keyword
match = soup.find("div", class_="footer")
print(match)


article = soup.find("div", class_="article")

# we can access the tags inside of other tags by chaining them together
print(article.h2.a.text)
print(article.p.text)

print()

# this method returns all the matches it finds for the given specifics as a list
# you can add class_ or id attributes to define the specifics
for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    summary = article.p.text

    print(headline)
    print(summary)
    print()
