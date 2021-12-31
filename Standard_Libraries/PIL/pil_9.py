from PIL import Image

img = Image.open(r"./Capture.JPG")

# you can see different modes here
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
img.convert(mode="L").show()
