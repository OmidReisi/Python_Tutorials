# requests is an external module and needs to be installed (pip install requests)
import requests

# sends a get request to the given url and returns a response object
r = requests.get(url=r"https://xkcd.com/353/")

print(r)

# help(r)

# returns the content of the response in unicode (usually it's html)
# print(r.text)

# if you're sending a request to a large file set stream = True in order to get the file byte by byte and not all at once (in order to preserve memory)
r = requests.get(url=r"https://imgs.xkcd.com/comics/python.png", stream=True)

# returns the content of the response in bytes
# print(r.content)

# you can use PIL library with io.BytesIO as well and then save the image but it's not necessary
with open(r"./Images/comic.png", "wb") as img_file:
    img_file.write(r.content)
