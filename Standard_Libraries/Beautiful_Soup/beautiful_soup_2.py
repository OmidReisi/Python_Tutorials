import requests
from bs4 import BeautifulSoup


source = requests.get(r"http://coreyms.com", timeout=10).text

soup = BeautifulSoup(source, "lxml")

# print(soup.prettify())

# you don't have to pass all the classes here we only pass the first class
# find method searches all tags so it doesn't matter if our article tag is nested in some other tags as well
article = soup.find(
    "article",
    class_="post-1670",
)
# print(article.prettify())


# we also could have said headline = article.a.text because the first a tag is the one we want
# when we say tag1.tag2 the tag2 doesn't have to be the exact children of tag1 it can be children of it's children
headline = article.h2.a.text
print(headline)


summary = article.find("div", class_="entry-content").p.text
print(summary)


# youtube videos have unique codes that are like this "https://www.youtube.com/embed/z0gguhEmWiY" and the part after the "embed" is their unique code
# in order to access an attribute of a tag you have to access them like a dictionary by passing the name of the attribute as a key
vid_code = (
    article.find("iframe", class_="youtube-player")
    .get("src")
    .split("/")[-1]
    .split("?")[0]
)
yt_link = f"https://youtube.com/watch?v={vid_code}"
print(yt_link)
