from PIL import Image
import os

for f in os.listdir(r"./Original_Images"):
    if f.endswith(".jpg"):
        i = Image.open(os.path.join("./Original_Images", f))
        file_name, file_ext = os.path.splitext(f)
        i.save(f"./Saved_Images/{file_name}.png")
