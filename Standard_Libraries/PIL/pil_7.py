from PIL import Image


img1 = Image.open(r"./Capture.JPG")

# this method returns a croped image based on a 4-tuple of (left,upper,right,lower)
# notice that in image cordinate-system the left and uppercordinates are 0 and comming down or going right increases the cordinate
print(img1.crop((100, 200, 1000, 800)).size)


img2 = Image.open(r"./Capture2.JPG")
print(img2.size)

# returns a copy of an image
img1_copy = img1.copy()

# pastes img2 on img1_copy
# the second argument can be a tuple of 4 or a tuple of 2 or None which represent (0,0)
# a tuple of 2 represents the upper left corner for starting position on img1_copy
# if you pass a box (tuple of 4) as second argument you're specifying the region of paste
# if you want to use a box as second argument the size of img2 should be same as size of the box
img1_copy.paste(img2, (50, 50))

img1_copy.show()


# rotating an image keeps the aspect ratio the same so you might lose the edges due to croping
# if you want to keep the whole image you have to set expand = True
img1.rotate(45, expand=True).show()
