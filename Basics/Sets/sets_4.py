l1 = [2, 1, 3, 1, 2, 3]

l2 = list(set(l1))
print(l2)

# for preserving order the following is the best way
l2 = list(dict.fromkeys(l1))
print(l2)
