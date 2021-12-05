message_1 = "Hello World"

# you can escape the ' by using \' or you can use "" instead.
message_2 = "Omid's world"

# """ is used for multi line strings and doc strings to keep the format of string over multiple lines.
message_3 = """Hello my name is Omid and 
I study Computer Engineering."""


print(message_1)
print(message_2)
print(message_3)

# len returns the number of items in a container
print(len(message_1))

# slicing [start:end:step] (start is included but end is excluded)
# default values : start = 0, end = end(-1), step = 1
print(message_1[8])

# returns string as lower case
print(message_1.lower())

# returns string as upper case
print(message_1.upper())

# returns the number of substring in the main string
print(message_1.count("Hello"))

# returns the start of substring in main string else -1
print(message_1.find("World"))

# replace the first substring wiht second substring
new_message = message_1.replace("World", "Universe")
print(new_message)

greeting = "Hello"
name = "Omid"

message = greeting + name
print(message)

message = greeting + ", " + name

print(message)

message = "{}, {}. Welcome!".format(greeting, name)

print(message)

message = f"{greeting}, {name}. Welcome!"

print(message)

print(dir(name))

print(help(str))

print(help(str.count))

# returns the unicode number for a single character
print(ord("!"))

print()

print(message_1.split("l", maxsplit=1))

print(message_1.strip("Hello"))
