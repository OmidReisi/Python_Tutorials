import itertools

# cycle method takes an iterable and cycles through it indefinitely
counter = itertools.cycle([1, 2, 3])


print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# repeat method returns an given item for times keyword argument (default indefinitely) if the iterator is exhausted more than times then a StopIteration error ocuurs
counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# map function returns an iterator that returns values of given function for iterables as that function arguments
# just like zip(), map() ends with the exhaustion of the shortest iterable
squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))

# starmap is like map function but instead of taking argument as seperated iterables takes them as an iterable that contains tuples of arguments
squares = itertools.starmap(pow, zip(range(10), itertools.repeat(2)))

print(list(squares))
