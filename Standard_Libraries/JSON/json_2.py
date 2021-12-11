import json
from os import sep

with open(r"./states.json", "r") as f:

    # this method loads a json file into a python object
    data = json.load(f)

for state in data["states"]:
    # print(state["name"], state["abbreviation"], sep=" - ")
    del state["area_codes"]


with open(r"./new_states.json", "w") as f:

    # this method dumps the python object into a json file
    json.dump(data, f, indent=2, sort_keys=True)
