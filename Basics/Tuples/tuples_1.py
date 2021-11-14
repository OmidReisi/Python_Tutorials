#  Unlike lists, Tuples are immutable which means they can't be modified

tuple_1 = ("History", "Math", "Physics", "CompSci")


tuple_2 = tuple_1

print(id(tuple_1))
print(id(tuple_2))

empty_tuple = ()
empty_tuple = tuple()
