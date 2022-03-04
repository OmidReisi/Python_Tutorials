# everything in python is an object(classes, instances of classes, functions, variables,...)
# type is the meta class used for creating new classes


# class A(object):
#     x = 13


# this line is the same as class A definition above.
# inherited classes are passed in a tuple
# attributes are passed in a dictionary
A = type("A", (object,), {"x": 13})
