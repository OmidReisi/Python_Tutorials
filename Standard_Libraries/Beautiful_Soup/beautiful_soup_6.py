import re
from bs4 import BeautifulSoup


with open(r"./Html/html_2.html") as f:
    doc = BeautifulSoup(f, "lxml")

# using regex to search for texts is very useful in web scrapping
tags = doc.find_all(text=re.compile(r"\$.*"))
for tag in tags:
    print(tag.strip())
