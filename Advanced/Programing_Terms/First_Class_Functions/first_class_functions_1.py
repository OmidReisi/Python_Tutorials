# First-Class Functions
# "A Programming language is said to have first-class functions if it treats functions as first-class citizens."

# First-Class Citizen (Programming):
# "A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the opeartions generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable."

# Higher-Order Functions
# "A higher-order function can have other functions as arguments or return them"


def square(x):
    return x * x


#  f now is same as square funciton
f = square

print(square)
print(f)
print(f(5))

# this a higher-order function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


def cube(x):
    return x * x * x


cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)

