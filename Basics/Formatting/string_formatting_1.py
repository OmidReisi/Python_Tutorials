person = {"name": "Jenn", "age": 23}

sentence = (
    "My name is " + person["name"] + " and I am " + str(person["age"]) + " years old."
)

print(sentence)

sentence = "My name is {} and I am {} years old.".format(person["name"], person["age"])
print(sentence)

# numbers in curly braces represent the order in format method
sentence = "My name is {0} and I am {1} years old.".format(
    person["name"], person["age"]
)
print(sentence)

tag = "h1"
text = "This is a headline"

sentence = "<{0}>{1}</{0}>".format(tag, text)
print(sentence)

# we can pass dictionary keys in placeholders as well
sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print(sentence)

li = ["Jenn", 23]
sentence = "My name is {0[0]} and I am {0[1]} years old.".format(li)
print(sentence)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jack", 33)

# we can access attributes of an instance with "."
sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)
print(sentence)

# we can pass in keyword arguments as well
sentence = "My name is {name} and I am {age} years old.".format(name="Jenn", age=30)
print(sentence)

# we can unpack list or dictionaries as well
sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence)

