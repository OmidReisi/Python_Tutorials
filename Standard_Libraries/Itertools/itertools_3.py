import itertools


letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

# returns an iterator that contains different combinations of r-lengthed tuples of the given iterable
# for combinations the order of elements DOES NOT MATTER (we see ("a", "b") but we don't see ("b", "a"))
result = itertools.combinations(letters, r=2)

for item in result:
    print(item)

# like combinations but the order of the elemnts matter (we see both ("a", "b"), ("b", "a"))
result = itertools.permutations(letters, r=2)

print()

for item in enumerate(result, start=1):
    print(item)

# returns the iterator of Cartesian product of given iterables (repeat is used when we want Cartisian product of one iterable multiple times)
result = itertools.product(numbers, repeat=4)

for item in enumerate(result):
    print(item)

# this is like combinations but allows the repetition of elements
result = itertools.combinations_with_replacement(names, r=4)

print("this is combinations_with_replacement of names")
for item in result:
    print(item)



