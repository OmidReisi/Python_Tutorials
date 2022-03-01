# from python 3.7+ if you want to use a type that has not been defined yet but will be in the future you have to import the following.
# remember that this import must always be the first import of your module.
from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    # the import above allows us to use type of Point inside of it because it's a future reference.
    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(5, 7)
p2 = Point(6, 9)
p3 = p1 + p2

print(p3.x)
print(p3.y)
