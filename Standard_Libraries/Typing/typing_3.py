from typing import Optional, Any, Sequence


# if an argument is optional, you should annotate it with Optional[type]
def foo(output: Optional[bool] = False) -> None:
    pass


# if you're argument can be any type, you should annotate it with Any
def bar(output: Any) -> None:
    pass


# a Sequence is any type that can be indexed.(list,tuple,dict,...)
# a string is a sequence because it can be indexed.
# a set is not a sequence because it is unordered and can't be indexed.
def myf(seq: Sequence[str]) -> None:
    pass


# this is general type tuple and this annotation is okey.
x: tuple = (1, 2, "hello")

# if you want to specify the type of items in a tuple, you should specify the type for each item individually.
y: tuple[int, int, int] = (1, 2, 3)
