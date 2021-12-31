from PIL import Image


img1 = Image.open(r"./Capture.JPG")
img2 = Image.open(r"./Capture.png")

# returns the format of image (png,jpeg,...)
print(img1.format)
print(img2.format)

# this returns the mode of an image (RGB, RGBA, L, ...)
# note that png has RGBA mode while jpeg has RGB mode so you can't save them instead of each other unless you convert them
print(img1.mode)
print(img2.mode)

# show the size of image in pixels in tuple of (width, height)
print(img1.size)
print(img2.size)


