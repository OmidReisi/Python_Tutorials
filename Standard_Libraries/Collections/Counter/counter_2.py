from collections import Counter


counter_1 = Counter(cats=4, dogs=5)


# this returns a iterator that generates keys as much as their values.
# a list of 4 cats and 5 dogs
print(list(counter_1.elements()))

# you can also assign them with negative values, in this case the key with negative value will not be added to the iterator.
counter = Counter(cats=4, dogs=-4)
print(list(counter.elements()))


# return a list of n length tuples of the most common elements.(n is the argument you pass)
print(counter_1.most_common(1))


# subtracts the given attribute from the Counter
counter.subtract(["cats", "dogs", "rats"])
print(counter)

# adds the given attribute to the Counter
counter.update(["cats", "dogs", "rats"])
print(counter)


# the following operations don't show keys that their values are <= 0

counter_1 = Counter(a=4, b=3, c=2, d=-3)
counter_2 = Counter(a=2, b=2, c=1, d=2)

# you can add and subtract Counters
print(counter_1 + counter_2)
print(counter_1 - counter_2)


# this acts like an intersection and returns values for min available between 2 Counters
print(counter_1 & counter_2)

# this finds the max between 2 counters and set it as their values.
print(counter_1 | counter_2)
