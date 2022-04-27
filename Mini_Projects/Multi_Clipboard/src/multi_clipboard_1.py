import sys
import json
from pprint import PrettyPrinter

# this module allows us to work with system's clipboard
import pyperclip

# # pastes the string that last you've copied to the clipboard.
# data = pyperclip.paste()
# print(data)

# # copies a string to the clipboard.
# pyperclip.copy("abc")
# print(pyperclip.paste())

PATH_TO_JSON_FILE = r"./clipbaord.json"

printer = PrettyPrinter(indent=2)


def save_data(filename: str, json_data: dict[str, str]) -> None:
    with open(filename, mode="w") as f:
        json.dump(json_data, f, indent=2, sort_keys=True)


def load_data(filename) -> dict[str, str]:
    try:
        with open(filename, mode="r") as f:
            json_data = json.load(f)
            return json_data
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    command: str = sys.argv[1]
    data = load_data(PATH_TO_JSON_FILE)
else:
    raise AttributeError(
        "only 1 of the following arguments should be passed for sys.argv: ('list', 'save', 'load', 'delete')"
    )


match command:
    case "save":
        key = input("Enter a key to store data: ")
        data[key] = pyperclip.paste()
        save_data(PATH_TO_JSON_FILE, data)
        print("Data Saved!")
    case "load":
        key = input("Enter a key to fetch it's data: ")
        if key in data:
            pyperclip.copy(data[key])
            print("Data Copied to Clipboard!")
        else:
            print("ERROR: Invalid Key")
    case "delete":
        key = input("Enter a key to to delete: ")
        if key in data:
            del data[key]
        else:
            print("KEY NOT FOUND")
        save_data(PATH_TO_JSON_FILE, data)

    case "list":
        print()
        printer.pprint(data)
        print()
    case _:
        print("ERROR: Invalid Command")
