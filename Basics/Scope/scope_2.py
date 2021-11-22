# below are some of the built-in variables

import builtins


# this lists all of built-in variables in python
print(dir(builtins))

# python allows us to overwrite built-ins so be careful
# def min():
#     pass


# finds the smallest value of an iterable
# if we overwrite the min function this line here wants to use our new min function and throws an error
m = min([5, 1, 4, 2, 3])
print(m)
