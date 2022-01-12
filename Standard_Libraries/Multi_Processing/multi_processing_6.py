import os
import time
from PIL import Image, ImageFilter
from collections import namedtuple

Img_Size = namedtuple("img_size", ["width", "height"])
size_1200 = Img_Size(width=1200, height=1200)
img_names = os.listdir(r"./Downloaded_Images")

start = time.perf_counter()

for img_name in img_names:
    with Image.open(fr"./Downloaded_Images/{img_name}") as img:
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size_1200)
        img.save(fr"./Processed_Images/{img_name}")
    print(f"{img_name} was processed successfully ...")

finish = time.perf_counter()

print(f"Program finished in {finish - start} seconds")
