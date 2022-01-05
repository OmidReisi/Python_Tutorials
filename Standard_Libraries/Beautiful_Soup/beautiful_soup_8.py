import requests
from bs4 import BeautifulSoup

url = r"https://coinmarketcap.com"

result = requests.get(url, timeout=10).text

doc = BeautifulSoup(result, "lxml")


tbody = doc.tbody

# this returns the list tags that are directly inside of the given doc(only looks for direct children)
# trs = tbody.find_all(recursive=False) this line does the same job as following
trs = tbody.contents


# you can access the next and previous neighbor of a tag on the same level with the following
# notice that when we try to get the sibiling before the first tag it returns None because there are no more sibilings on the same level before this tag
# print(trs[0].previous_sibling)

# print(trs[0].next_sibling.prettify())

# next_sibilings and previous_sibilings work the same way but they return an iterator that contains all of the tags that are before or after the given tag
# as you can see this is still an empty list
# print(list(trs[0].previous_siblings))

# print(list(trs[90].next_siblings))

# .parent returns the parent tag
# you can get the name of a tag with .name
# print(trs[0].parent.name)


# this returns an iterator containing everything(it means children tags recursively and contents of each tag) that comes inside of the tag
# tr_d = trs[0].descendants
print()

# for item in tr_d:
#     print(item, type(item), sep="\t\t")
#     print()
#     print()
#     print()

# this is same as .contents but returns an iterator instead (only looks for direct children tags)
# tr_c = trs[0].children

# for item in tr_c:
#     print(item, type(item), sep="\t\t")
#     print()
#     print()
#     print()
