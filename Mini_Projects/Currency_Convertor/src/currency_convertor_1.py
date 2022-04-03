import os
from pprint import PrettyPrinter
import requests
from dotenv import load_dotenv


load_dotenv(r"./api/api_key.env")

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://free.currconv.com/"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = requests.get(url, timeout=7).json()

    data = data["results"]
    data = dict(sorted(data.items(), key=lambda item: item[0]))

    return data


def currency_display(currencies):
    for currency in currencies.values():
        name = currency["currencyName"]
        _id = currency["id"]

        # if the key doesn't exist the default value (empty string) is returned.
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency_1, currency_2):
    endpoint = (
        f"api/v7/convert?q={currency_1}_{currency_2}&compact=ultra&apiKey={API_KEY}"
    )
    url = BASE_URL + endpoint
    data = requests.get(url, timeout=7).json()
    printer.pprint(data)


# currency_data = get_currencies()
# currency_display(currency_data)

exchange_rate("USD", "IRR")
