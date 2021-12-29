import itertools

# this module contains operators like (+, *, ...) as functions and we can use them for situations we want to pass them as functions
import operator


numbers = [1, 2, 3, 4, 2, 1, 0]

# return the accumalation of values for the given func(the default func is +)
result = itertools.accumulate(numbers, func=operator.mul)


for item in result:
    print(item)
