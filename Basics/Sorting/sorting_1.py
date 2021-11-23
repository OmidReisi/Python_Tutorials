li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# sorted function returns a new list and does not alter the original list
s_li = sorted(li)

print("Sorted Variable:\t", s_li)
print("Original Variable:\t", li)

# sort method does not return a new list and sort the same list in place
# li.sort()
# print("Original Variable:\t", li)
print()

s_li = sorted(li, reverse=True)

print("Sorted Variable:\t", s_li)
print("Original Variable:\t", li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

# tuples are immutable and don't have sort methods
# sorted function always returns a list no matter what it gets as an argument
s_tup = sorted(tup)

di = {"name": "Omid", "job": "Programming", "age": None, "OS": "Windows11"}

# when we sort dictionaries we just get the keys in sorted order
s_di = sorted(di)
print(s_di)

print()

li = [-6, -5, -4, 1, 2, 3]

s_li =sorted(li, key= abs)

print("Sorted Variable:\t", s_li)
print("Original Variable:\t", li)