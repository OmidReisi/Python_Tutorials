def match_list(li):
    match li:
        # this is how we check if a value is in a list of specified items.
        case [x, (1 | 2 | 3 | 4) as num]:
            print("a list of 2 and the second number is in range of 4")
        case [x, y]:
            print("list of two in x, y")
        # this is just unpacking a and means that a list of 3 or more.
        case [x, y, z, *a]:
            print("list of three or more")


match_list([1, 7])
