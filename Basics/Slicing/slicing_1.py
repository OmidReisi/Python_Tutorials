my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# -10, -9, -8, -7, -6, -5, -4, -3, -2, -1

# end is non-inclusive
# step's default value is +1
# list[start:end:step]

print(my_list[0:6])

print(my_list[-7:-2])

# returns an empty list because -2 is bigger than -7 and we need to specify step as negative number
print(my_list[-2:-7])

# even though 2 is bigger than -1 python recognizes that -1 here represents 9 and converts it to it
print(my_list[2:-1])

# one rule that it important is that if indexing goes out of lists range you get an empty list as result
print(my_list[-1:2:-1])
