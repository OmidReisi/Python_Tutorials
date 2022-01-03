# STRING_INTERPOLATION is the usage of adding placeholders in strings and using different variables to replace them
# remember that string concatenation is different from string interpolation


name = "omid"
age = 21

# this is string concatenation
greeting = "My name is " + name + " and I am " + str(age) + " years old."
print(greeting)

# this is string interpolation
greeting = f"My name is {name} and I am {age} years old."
print(greeting)
