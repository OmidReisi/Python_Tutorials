def add(x, y):
    """Add Function

    Args:
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x + y


def subtract(x, y):
    """Subtract Function

    Args:
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x - y


def multiply(x, y):
    """Multiply Function

    Args:
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x * y


def divide(x, y):
    """Divide Function

    Args:
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x / y


num_1 = 10
num_2 = 5

# this way we just print the results and no logging is used and it's not fun

add_result = add(num_1, num_2)
print("Add : {} + {} = {}".format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
print("Add : {} - {} = {}".format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
print("Add : {} * {} = {}".format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
print("Add : {} / {} = {}".format(num_1, num_2, div_result))
