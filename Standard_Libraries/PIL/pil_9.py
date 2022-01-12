from PIL import Image
import io

img = Image.open(r"./Capture.JPG")

# you can see different modes here
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
# img.convert(mode="L").show()

# this returns image as raw bytes and you can't convert them back to an Image object
img_bytes = img.tobytes()

# this is another way to get the image bytes but it's not raw and you can turn them back to an Image object with io.BytesIO(bytes)
bytes_arr = io.BytesIO()
img.save(bytes_arr, format=img.format)
bytes_arr.getvalue()
