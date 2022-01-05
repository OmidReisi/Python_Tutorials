from bs4 import BeautifulSoup

with open(r"./Html/html_2.html") as f:
    doc = BeautifulSoup(f, "lxml")


# print(doc.prettify())
tag = doc.find("option")

# print()
# print()

# you can access attributes of a tag like a dictionary and modify them here
# just like tags modifying attributes affects the whole document
# tag["selected"] = "false"

# you can also add attributes to a tag the same way you way
# tag["new_attr"] = "new value"
# print(doc.prettify())


# returns a dictionary of all attributes of the given tag
print(tag.attrs)

# passing a list of tags to find_all returns all of the occurences of them as a list(serches for multiple tags)
# if you pass a list of tag to find method it returns the first tag of that it sees first in the doc tree
# it lists them by the order it finds them not by the order of the given tags
tags = doc.find_all(["p", "div"])

# for tag in tags:
#     print(tag, end="\n\n\n\n")

# you can mix searching for tags and texts at the same time
# this returns all the option tags that have the text "Undergraduate" in them
tags = doc.find_all("option", text="Undergraduate")
print(tags)

# you can also add different attributes as keyword arguments to search for the tags
tags = doc.find_all(["option"], value="undergraduate")
print(tags)

# if you only want to check for the existence of attributes and don't care about their value use True as their value
# you can also use lambda functions and set it to True for the values you want
tags = doc.find_all("option", value=True)
print(tags)

# tags = doc.find_all("option", value=lambda attr: attr != "undergraduate") this is same as below
tags = doc.find_all("option", value=lambda attr: "undergraduate" not in attr)
print(tags)


print()
print()
print()
print()


# you don't have to pass any argument to find_all method in this case it returns all the tags
tags = doc.find_all()
print({tag.name for tag in tags})

print()
print()

# when you want to return tags that are not of the given class you should always check for the existence of the class first
# this returns all tags that don't have a class or they don't have "btn-item" as one of their classes
tags = doc.find_all(class_=lambda c: c == None or "btn-item" not in c)
for tag in tags:
    print(tag)
    print()
    print()
