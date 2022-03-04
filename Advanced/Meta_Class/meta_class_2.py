# by default the meta class used for creating other classes is type.


# to create meta classes it's better that they inherit from type
# __new__  is the method that constructs the class and is called before __init__
# you can change the way the class is constructed in this __new__ method.(e.g. changing the names of the attributes of the class)
class meta(type):
    def __new__(cls, name, bases, attrs):
        a = {attr.upper(): attrs[attr] for attr in attrs.keys()}
        return type(name, bases, a)


#
class A(metaclass=meta):
    var = 14


a1 = A()

# here because we uppercased the letters of the attributes  "x" is not an attribute anymore and it's converted to "X"
print(a1.VAR)
