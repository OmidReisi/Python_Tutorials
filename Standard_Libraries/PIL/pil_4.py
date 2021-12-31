from PIL import Image, ImageFilter


image1 = Image.open(r"./Original_Images/image_1.jpg")

# rotate() method rotates an image by the given degree counter-clock wise and returns the new image object
image1.rotate(90).show()

# convert() method returns a converted image
# mode= "L" means return a new black and white image
image1.convert(mode="L").show()

# filter method puts some filter on out image and returns a new image object
# ImageFilter.GaussianBlur is a filter that makes our image blur(the default value of radius is 2 and increasing it makes image more blury)
image1.filter(ImageFilter.GaussianBlur(radius=10)).show()
