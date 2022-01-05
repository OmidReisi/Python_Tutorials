from bs4 import BeautifulSoup


with open(r"./Html/html_2.html") as f:
    doc = BeautifulSoup(f, "lxml")

tags = doc.find_all("input", type="text")

for tag in tags:
    tag["placeholder"] = "I changed you!"

# you can save beautifuloup objects in an html file you just have to convert them to strings
with open(r"./Html/html_2_modified.html", "w") as f:
    f.write(str(doc))
