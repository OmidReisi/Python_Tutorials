import itertools

# returns a counter iterator that counts by step( default is 1), from start (default is 0)
counter = itertools.count()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# for num in counter:
#     print(num)

data = [100, 200, 300, 400]

# zip returns an iterator that puts the i-th argument of each iterable in a tuple
daily_data = list(zip(itertools.count(start=1, step=1), data))

print(daily_data)

# just like zip function but this one ends on the longest iterable
# fillvalue is used for those iterables that come up short and the default is NONE
daily_data = list(itertools.zip_longest(range(10), data, fillvalue="NO Value"))

print(daily_data)
