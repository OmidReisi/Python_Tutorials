from collections import Counter

# this takes an iterable and returns a dict with items in the iterable as keys and their counts as values.
# all the dict method are available for the type counter as well
counter_1 = Counter("ababccbbaacabccabcccabacdddbddda")


# if an item doesn't exist in the Counter than 0 is returned as it's value. (doesn't raise an error)
print(counter_1["h"])

# you can also create Counter objects with dictionaries as well.
counter_2 = Counter({"a": 5, "b": 6})
print(counter_2)

# you also can create Counter objects with assigning values to  keys without surrounding the keys with quotes.
counter_3 = Counter(a=5, b=6)
print(counter_3)
