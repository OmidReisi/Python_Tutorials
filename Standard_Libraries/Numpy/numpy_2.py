import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], dtype=np.int16)


# you can index arrays with [row, column]
# if you index with [row] you're refrencing the whole row
print(a[0])

print(a[1, 5])

# another way to refrence the whole row
print(a[1, :])

# refrencing the whole column
print(a[:, 4])

# from the first row's second element to the last element of the first row (excluding) with step of 2
print(a[0, 1:-1:2])


# just like lists numpy arrays are mutable.
a[1, 5] = 20
print(a)

print()

# if you set a part of the array a single value then all the elements of that part get that value
# or you can set the part to a list of the same size of the part
a[0] = [5]
print(a)
