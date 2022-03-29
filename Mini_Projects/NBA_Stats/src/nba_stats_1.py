# this allows us to print json in terminal with indentation.
from pprint import PrettyPrinter

import json
import requests

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

data = requests.get(BASE_URL + ALL_JSON, timeout=5).json()

print()

# # or you can use json module to pretty print the data
# json_str = json.dumps(data, indent=4, sort_keys=False)
# print(json_str)

printer = PrettyPrinter(indent=2)
# printer.pprint(data)

links = data.get("links")
# printer.pprint(links)

scoreboard = links.get("currentScoreboard")
# print(scoreboard)


def get_scoreboard():
    scoreboard_data = requests.get(BASE_URL + scoreboard, timeout=5).json()
    games = scoreboard_data.get("games")
    # printer.pprint(games)
    for game in games:
        print(
            f"{game['hTeam']['triCode']}({game['hTeam']['score']}) - {game['vTeam']['triCode']}({game['vTeam']['score']})"
        )
        print("----------------------------------------------------------")


get_scoreboard()
