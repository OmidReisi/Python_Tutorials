# when an argument can have multiple types we use Unions in python 3.9 and below.
# in python 3.10 and above we use piping to seperate the different types.

from typing import Union


# this is how we do it in python 3.10 and above.
def add(x: int | float, y: int | float) -> int | float:
    return x + y


# this is how we do it in python 3.9 and below.
def sub(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x - y


# in python 3.10 it's convention to use | None instead of Optional for optional arguments.
def foo(output: bool | None = False) -> None:
    pass

foo(True)