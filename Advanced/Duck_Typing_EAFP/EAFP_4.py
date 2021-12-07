my_list = [1, 2, 3, 4, 5, 6]

# LBYL (NON-PYTHONIC)
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index does not exist")


# EAFP (PYTHONIC)
try:
    print(my_list[5])

except KeyError as e:
    print(e)
