import itertools


numbers = [0, 1, 2, 3, 2, 1, 0, 1]


def lt_2(n):
    if n < 2:
        return 2
    return False


# returns an iterator that contains items of the iterable that come after the first False of the function
result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)

print()
print()

# opposite of dropwhile takes items of iterable untill it hits the first false
result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)



