import requests
from bs4 import BeautifulSoup
from itertools import islice

url = r"https://coinmarketcap.com"

result = requests.get(url, timeout=10).text


doc = BeautifulSoup(result, "lxml")


table_rows = islice(doc.tbody.children, 10)

for table_row in table_rows:

    name = table_row.contents[2].a.p.text
    price = table_row.contents[3].a.text

    print(name, price, sep=": ")
    print()
