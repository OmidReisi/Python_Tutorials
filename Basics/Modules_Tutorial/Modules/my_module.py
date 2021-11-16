print("Imported my_module ...")

test = "Test String"


def find_index(to_search, target):

    """find the index of target in to search list

    Args:
        to_search (iterable): an iterable to search index
        target (any): value to search for
    """

    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


print(__name__)
