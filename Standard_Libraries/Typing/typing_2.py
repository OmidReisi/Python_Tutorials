# import typing

# before python 3.9 python types like list, dict and ... couldn't be used as type annotations.
# for python 3.8 and below you should use typing.List or typing.Dict or ... for type annotations.(from typing import List, Dict, Set)
x: list[list[int]] = []
y: dict[str, str] = {"a": "b"}

# you can give a new name to your complicated types and use that name in annotations.
vector = list[float]
vectors = list[vector]


def foo(v: vector) -> vector:
    return v


def bar(b: vectors) -> vector:
    return b[0]
