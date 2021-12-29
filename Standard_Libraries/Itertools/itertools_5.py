import itertools


letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3, 4]

selectors = [True, True, False, True]

# takes an iterable and returns an iterator containing elements from the first iterable that corresponds to True by the second(selector) iterable
# works somewhat like filter() function but instead of using another function like filter(), compress uses another iterable to determine True or False
result = itertools.compress(letters, selectors=selectors)

for item in result:
    print(item)


def lt_2(n):
    if n < 2:
        return 2
    return False


# returns an iterator that contains items from the iterable that return true for the given function
result = filter(lt_2, numbers)

for item in result:
    print(item)

print()

# just like filter function instead it returns items that evaluate to false
result = itertools.filterfalse(lt_2, numbers)

for item in result:
    print(item)
