from collections import namedtuple

# this syntax creates an semi-object called Color that functions just like a tuple but has named fields
# the name we pass in as an argument is better to be same as our object variable
Color = namedtuple("Color", ["red", "green", "blue"])

color_1 = Color(44, 33, 66)

print(color_1)
print(color_1[0])

color_2 = Color(red=78, green=32, blue=84)

print(color_2)
print(color_2.blue)


white = Color(red=255, green=255, blue=255)

print(white)
