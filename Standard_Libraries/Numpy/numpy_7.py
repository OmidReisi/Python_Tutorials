import numpy as np

file_data = np.genfromtxt(r"./data.txt", delimiter=",")

# an array of bools with the shape of the original array.
print(file_data > 50)

print()

# an array of size of a row of original array where all the elements in each column or bigger than 50 or not
print(np.all(file_data > 50, axis=0))

print()

print(np.any(file_data > 50, axis=1))

print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# note that you can pass an array for indexing as well
print(a[[1, 2, 4, 6]])
# same as above we're selecting two elements multiple times.
print(a[[1, 0, 1, 1, 0, 0, 0, 1]])

# but if you pass a list of True and False it contains elements that their position is True.
print(a[[True, False, False, False, True, False, False, True]])

print()

# select only when condition is true
print(file_data[file_data > 100])

print()


# and for two conditions
print((file_data > 50) & (file_data < 100))

print()

# or for two conditions
# use ~ for not conditions
print(~((file_data > 50) | (file_data < 20)))


# for indexing 2d or more dimensions with lists pass elements into different lists for dimensions.
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# selecting elements a[0,2], a[1,2], a[0,4], a[1,4]
print(a[[0, 1, 0, 1], [2, 2, 4, 4]])
