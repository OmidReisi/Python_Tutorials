import numpy as np

# creating the following matrix

# [1,1,1,1,1
# 1,0,0,0,1
# 1,0,9,0,1
# 1,0,0,0,1
# 1,1,1,1,1]

output = np.ones((5, 5))

z = np.zeros((3, 3))

z[1, 1] = 9

output[1:-1, 1:-1] = z

print(output)
print()

# be careful arrays are mutable and if two names point to the same array changing one changes another.

a = np.array([[1, 2, 3], [4, 5, 6]])

b = a

b[1] = 0
print(b)
print()
print(a)
print()

# use copy method when you want to copy an array.
b = a.copy()

b[0] = 0

print(b)
print()
print(a)
