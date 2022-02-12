from typing import TypeVar

# you can create new types with this method (generic type)
# inside the method we pass the name we want to give to the type.(usually it's the same as the variable you use for it.)
# generic types are usually used when we want to use a specific type but we don't know what that type is exactly.in other words there is only one type but it's unclear what type it actually is.
T = TypeVar("T")


def get_item(lst: list[T], index: int) -> T:
    return lst[index]
