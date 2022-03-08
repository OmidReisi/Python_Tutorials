import numpy as np

# numpy is a built-in module that has all the tools needed for statistics and math operations and is the base module for pandas library
# numpy arrys are faster than lists and for 2d arrays it's better to use numpy.

# use np.array when all arrays have the same number of elements
a = np.array([1, 2, 3, 4])

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])


# returns the number of dimensions of the array
print(a.ndim)
print(b.ndim)


# returns a tuple of width(number of dimensions) and height(number of items in each array).
# if it's a 1d array, then this shows only the number of dimensions.
print(a.shape)
print(b.shape)

# size of each element in np.array
print(a.itemsize)
print(b.itemsize)

# type of each element in np.array
print(a.dtype)
print(b.dtype)

# total number of elements in the np.array
print(a.size)
print(b.size)

# total number of size of the np.array (size * itemsize)
print(a.nbytes)
print(b.nbytes)


# you can specify a type for the array elements
c = np.array([1, 2, 3, 4], dtype="int16")
