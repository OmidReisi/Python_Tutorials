# pillow allows us to work with images in python
# pillow is not a built-in library and needs to be installed (python -m pip install --upgrade pillow)

from PIL import Image

# this returns our image object and we can store it in a variable
image1 = Image.open(r"./Original_Images/image_1.jpg")

# shows the image object to the screen
image1.show()

# this save the image under a different name
image1.save(r"./Saved_Images/image_1.png")
