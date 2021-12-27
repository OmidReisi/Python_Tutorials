s1 = {1, 2, 3, 4, 5, 1, 2, 3}

s2 = {7, 8, 9}
s1.add(6)

# update a set with one or more iterables
s1.update([7, 8], s2)

print(s1)

# same as each other but remove raises an error if it is not a member
s2.remove(7)
s2.discard(6)
