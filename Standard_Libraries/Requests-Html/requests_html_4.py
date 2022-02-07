from requests_html import HTML, HTMLSession

session = HTMLSession()

r = session.get(r"https://coreyms.com/")


# returns a set of all the links available in the given web page or element
# print(r.html.links)

# for link in r.html.links:
#     print(link)


# if there are relative links in the element or the given webpage use absolute_links the get the full link
for link in r.html.absolute_links:
    print(link)
