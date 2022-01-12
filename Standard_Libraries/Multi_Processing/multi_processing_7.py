import os
import time
import concurrent.futures
from PIL import Image, ImageFilter
from collections import namedtuple

Img_Size = namedtuple("img_size", ["width", "height"])
size_1200 = Img_Size(width=1200, height=1200)
img_names = os.listdir(r"./Downloaded_Images")


def img_processing(img_name):
    with Image.open(fr"./Downloaded_Images/{img_name}") as img:
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size_1200)
        img.save(fr"./Processed_Images/{img_name}")
    return f"{img_name} was processed successfully ..."


if __name__ == "__main__":

    start = time.perf_counter()

    # we can see that using multiprocessing speeds up the process drastically (although this image processing is still more I/O BOUND than CPU BOUND and it' better to use threading instead of multiprocessing)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(img_processing, img_names)
        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Program finished in {finish - start} seconds")
