import numpy as np

a = np.array([[-1, 4, -2, 6, 89, 3, 9], [-6, -3, 2, 5, 1, 98, 5]])

# if axis=1 returns an array size of the dimension of original array that contains the smallest number from each array of dimension.(height of smallest widths)
# if axis=0 returns an array size of the sub_arrays of original array that contains the smallest number from each dimension.(width of smallest heights)
# if no axis is defined, returns the smallest number of whole array
print(np.min(a, axis=1))

print(np.max(a, axis=0))


print(np.sum(a, axis=0))
print()


# in order to reshape an array shape must contain all the values of the original array.
a_reshaped = a.reshape((7, 2))
print(a_reshaped)

print()


# if 2 arrays have the same dimension you can vertically stack them together.(you have to pass the arrays as a list or a tuple.)
print(np.vstack((a[0], a[1], a[0], a[0])))

print()


a = np.ones((2, 4))
b = np.zeros((2, 2))

print(np.hstack((a, b)))

print()
print()

# you can read data from a txt file by passing a delimiter.
file_data = np.genfromtxt(r"./data.txt", delimiter=",")

print(file_data)

print()
print()

# copis an array with different data type.
int_file_data = file_data.astype(np.int16)

print(int_file_data)
