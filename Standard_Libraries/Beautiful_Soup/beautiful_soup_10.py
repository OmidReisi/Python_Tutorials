import requests
import re
import csv
from bs4 import BeautifulSoup


gpu_name = input("Enter the name of the GPU you want to search for : ")

url = fr"https://www.newegg.com/p/pl?d={gpu_name}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "lxml")


number_of_pages = int(
    doc.find("span", class_="list-tool-pagination-text").strong.text.split("/")[-1]
)

# a list to store all of our items as a dictionary with their names, prices and links
items_found = []

for page in range(number_of_pages):
    url = fr"https://www.newegg.com/p/pl?d={gpu_name}&N=4131&page={page+1}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "lxml")
    div = doc.find("div", class_="list-wrap")

    items = div.find_all(text=re.compile(gpu_name))

    for item in items:
        item_parent = item.parent

        try:
            item_name = item_parent.text
            link = item_parent["href"]
            # find_parent method goes up the doc tree and looks for the parent with the given specifics(also looks for the parent of parents and returns the first parent that matches our search)
            # this is same as main_parent = item_parent.parent.parent
            main_parent = item.find_parent(class_="item-container")
            # there are some more information like the offers after the price so we're removing everything after the price
            price = main_parent.find("li", class_="price-current").text.split()[0]
            # here we remove the $ and , from our prices to turn them into numeric values
            # pattern = re.compile(r"[$,]")
            # price = float(pattern.sub("", price))
            items_found.append({"Name": item_name, "Price": price, "Link": link})

        except Exception:
            continue


print(len(items_found))

items_found_sorted_by_price = sorted(items_found, key=lambda d: d["Price"])


# for item in items_found_sorted_by_price:
#     print(item, end="\n\n")


with open(fr"./{gpu_name}.csv", mode="w", encoding="utf8", newline="") as file:
    csv_writer = csv.DictWriter(
        file, fieldnames=["Name", "Price", "Link"], delimiter=","
    )
    csv_writer.writeheader()
    for item in items_found_sorted_by_price:
        csv_writer.writerow(item)
