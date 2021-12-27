s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# return a set containing elements that are in all sets
s4 = s1.intersection(s2)
print(s4)

# return a set containing elemnts of s1 that are NOT in any other set
s4 = s1.difference(s2)
print(s4)

# (s1 - s2) + (s2 - s1)
s4 = s1.symmetric_difference(s2)
print(s4)
