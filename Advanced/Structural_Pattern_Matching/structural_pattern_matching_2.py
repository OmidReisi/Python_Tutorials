def check_coords(coords):
    match coords:
        case (0, 0):
            print("Origin")

        # this checks for a tuple of two that the first item is 0 and stores the second item in y
        case (0, y):
            print(f"Vertical line at y={y}")

        case (x, 0):
            print(f"Horizontal line at x={x}")
        # you can also use if statements in each case for more details.
        case (x, y) if x == y:
            print("X = Y")
        case (x, y) if abs(x) == abs(y):
            print("|x| = |Y|")
        # this checks for a tuple of two but does not store the items in any variable.
        case (_, _):
            print("Valid Coords")
        case _:
            print("Invalid Coords")


check_coords((4, 5))
