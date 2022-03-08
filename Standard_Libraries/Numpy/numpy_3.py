import numpy as np


# a matrix of 0 with the given shape
# you can specify dtype for as well
a = np.zeros((2, 3))
print(a)

print()

# a matrix of 1 with the given shape
b = np.ones((3, 5), dtype=np.int8)
print(b)


# same as np.ones and np.zeros but you specify the value to fill the matrix with.
# you can specify 3d or more dimensions as well by adding a dimension to the shape
c = np.full((4, 3, 2), 8)

print()

print(c)


print()
print()

# random values between [0,1)
# note that you pass the shape of array as different integer numbers and not a tuple
# if no argument is given returns a single random number
d = np.random.rand(4, 5)
print(d)

print()

# just like above but you can pass shapes as tuples as well
e = np.random.random_sample(a.shape)
print(e)

print()
print()

# random integers between [a,b) with the given size
# size can be None or a single integer
# if a is not defined it defaults to zero
f = np.random.randint(7, size=(4, 5))
print(f)

print()

# identity square matrix
I = np.identity(6)
print(I)


print()


g = np.array([[1, 2, 3]])

# if you want to repeat this array over each other you have to specify the original array as 2d and set the axis to 0
h = np.repeat(g, 3, axis=0)

print(h)
