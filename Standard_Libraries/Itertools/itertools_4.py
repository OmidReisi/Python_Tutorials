import itertools


letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

# takes some iterables as arguments and chains them together to conduct an iterator untill all iterables are over
combined = itertools.chain(letters, numbers, names)


for item in combined:
    print(item)

# returns an iterator that slices the given iterable(works like list slicing)
# islice(iterable, start=0, end, step=1)
result = itertools.islice(range(10), 2, 7, 2)

for item in result:
    print(item)


print()
print()
print()

# files are actualy iterators themselves and the next() function returns the next line
with open(r"./test.log", "r") as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end="")
