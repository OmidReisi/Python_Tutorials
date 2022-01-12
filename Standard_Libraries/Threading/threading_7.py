import requests
import time


# without using threading it takes so long to download these images
# unsplash is a website that has high resolution images that are free to use

img_urls = [
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
    "https://images.unsplash.com/photo-1532009324734-20a7a5813719",
    "https://images.unsplash.com/photo-1524429656589-6633a470097c",
    "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79",
    "https://images.unsplash.com/photo-1564135624576-c5c88640f235",
    "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6",
    "https://images.unsplash.com/photo-1522364723953-452d3431c267",
]

start = time.perf_counter()


for img_url in img_urls:
    img_data = requests.get(img_url).content
    img_name = "-".join(img_url.split("/")[-1].split("-")[:-1])
    with open(fr"./Downloaded_Images/{img_name}.JPEG", "wb") as img:
        img.write(img_data)
    print(f"{img_name} was downloaded successfully.")


finish = time.perf_counter()

print(f"Program finished in {finish - start} seconds.")
