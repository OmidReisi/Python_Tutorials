# JSON stands for JavaScript Object Notation but it is independent of JavaScript and is used for storring data and settings

import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

# this method returns a json object converted to a python object from a string
data = json.loads(people_string)

print()
# print(data)

# python uses the table in the link below to convert json objects into python objects
# https://docs.python.org/3/library/json.html#encoders-and-decoders

# this returns a type of dictionary
# print("\n", type(data))

# print(data["people"])


for person in data["people"]:
    del person["phone"]

# this method takes a python object and reverts it back to a json object as a string
# you can pass an indent keyword argument as well which specifies the indentattion for each level
# sort_keys is another keyword argument which specifies if the keys should be sorted alphabetically
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
