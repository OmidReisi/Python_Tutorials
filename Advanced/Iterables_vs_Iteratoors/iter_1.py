nums = [1, 2, 3]

for num in nums:
    print(num)

# lists, tuples, sets, dicts are iterables because they can be looped through and they have a special method called __iter__
print(dir(list))

# iterators are objects that know the state they're in and how to get their next value
# iterators are recognized with their special __next__ method which returns their next value
# lists, tuples, sets, dicts are NOT iterators because they don't have __next__ method


# iterables can become iterators when we run their __iter__ method
i_nums = nums.__iter__()

# __next__ and __iter__ methods  can be called with  iter() and next() functions which is the better and more clean way of calling them
# iterators are also iterables as well and their __iter__method returns themselves
# so in short: ITERABLES: objects that have an __iter__ method, ITERATORS: iterables that have a __next__ method


print(next(i_nums))

# when iterators reach their final state asking for their next value throws a StopIteration error

# casting an iterator to an iterable only casts values from the next value forward because iterators don't have access to their previous states.
l1 = list(i_nums)

print("this is l1", l1)
