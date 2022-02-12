from typing import Callable


# if you want to pass a funcion as a parameter you should use Callable[], and inside the square brackets define the type of arguments and return type of said Callable.
def foo(func: Callable[[int, int], int]) -> int:
    return func(1, 2)


def add(x: int, y: int) -> int:
    return x + y


print(foo(add))


# if you want to add annotations for lambda funcions you should do it like below
# now use the func instead of lambda
func1: Callable[[int, int], int] = lambda x, y: x + y
