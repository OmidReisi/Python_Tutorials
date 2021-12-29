import itertools

# this is like attrgetter but used for dicts to get their keys
from operator import itemgetter


people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
    {"name": "Omid Reisi", "city": "Manhatan", "state": "NY"},
]

# people = sorted(people, key=lambda person: person["state"])
people.sort(key=itemgetter("state"))

# print(people)

# returns an iterator containing tuples of (key,grouper)
# key in the tuple is the different values returned from the key argument in the groupby method
# groupby only works if the elements of iterable are already sorted by the key you want to pass as key argument (for example adding another person that has state="NY" to the end of the list creates another group for it)
person_group = itertools.groupby(people, key=itemgetter("state"))

# for key, group in person_group:
#     print(key)
#     for person in group:
#         print(person)
#     print()

# takes an iterable and returns an n-length tuple containing copies of the given iterators (n is not a keyword argument and specifies the number of copies and it's default is 2)
# after copying, the original iterator (if it is an iterator) should never be used because it might cause problems for exhaustion of other copies
copy_1, copy_2 = itertools.tee(person_group, 2)
