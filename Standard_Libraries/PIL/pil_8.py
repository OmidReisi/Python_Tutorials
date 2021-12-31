from PIL import Image

img = Image.open(r"./Capture.JPG")

# this method returns a new transposed image
# this one flips it left to right
img.transpose(Image.FLIP_LEFT_RIGHT).show()


img.transpose(Image.FLIP_TOP_BOTTOM).show()

# remember that rotation works counter-clock wise
img.transpose(Image.ROTATE_90).show()
