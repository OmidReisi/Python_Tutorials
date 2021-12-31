from PIL import Image
import os
from collections import namedtuple

Image_size = namedtuple("size_of_Image", ["width", "height"])

size_300 = Image_size(width=300, height=300)

for f in os.listdir(r"./Original_Images"):
    if f.endswith(".jpg"):
        i = Image.open(os.path.join("./Original_Images", f))
        file_name, file_ext = os.path.splitext(f)

        # thumbnail method allows us to make thumbnails and resize images
        i.thumbnail(size=size_300)
        i.save(f"./Saved_Images/{file_name}_300.jpg")
