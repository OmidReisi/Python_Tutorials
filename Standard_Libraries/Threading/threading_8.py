import requests
import time
import concurrent.futures

# we can see that using threading for I/O BOUND problems like downloading these images we speed up the process drastically

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


def img_downloader(img_url):
    img_data = requests.get(img_url).content
    img_name = "-".join(img_url.split("/")[-1].split("-")[:-1])
    with open(fr"./Downloaded_Images/{img_name}.JPEG", "wb") as img:
        img.write(img_data)
    return f"{img_name} was downloaded successfully."


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(img_downloader, img_urls)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Program finished in {finish - start} seconds.")
