import requests
from bs4 import BeautifulSoup


r = requests.get(
    r"https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-xtreme-12g/p/N82E16814932440"
)


doc = BeautifulSoup(r.text, "lxml")


# if you want to search for a text instead of a tag use the text keyword
prices = doc.find_all(text="$")

# as you can see the following just shows a list with 2 $ and nothing else
# Beautiful soup is set up in a tree structure and we can access parents and children of each tag and text
# parent of texts are the tag that they are in

# you can access parent of texts with parent attribute
parent = prices[0].parent
print(parent.text)
