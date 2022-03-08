import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])


# you can do math operations on numpy arrays.

print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)

print()
print(a + b)
print(a - b)
print(a * b)
print(a / b)


d = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])

# sin of every elment in radians rounded to 2 decimal points
print(np.round(np.sin(d), 2))

print()

# matrix multiplication of two matrixs : (a,b), (b, c) -> (a,c)
a = np.ones((4, 3))
b = np.full((3, 6), 4)

print(np.matmul(a,b))
