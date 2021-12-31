from PIL import Image


img = Image.open(r"./Capture.JPG")

# this method takes a tuple of (width, height) and returns an new image with that size
# this method doesn't keep the aspect ratio and uses the size tuple strictly and aspect ratio might change
# it can blow images up and changes the size of image strictly by the given size
small_img = img.resize((200, 300))
print(small_img.size)
small_img.show()

# same as resize but does not return an new image and resizes in place
# unlike resize this keeps the aspect ration the same and uses the width in tuple strictly and sets the height of image based on aspect ratio (height of image might not be same as given height in tuple)
# if you give a size bigger than the originl image it does not change the size of image (can't blow images up)
img.thumbnail((200, 300))
print(img.size)

# as you can see height of image has changed based on the aspect ratio and is not same as given height in tuple
img.show()
