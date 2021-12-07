# being pythonic means that you follow the conventions and codingy styles of python to write clean code.

# Duck_Typing : if an object walks like a duck and quacks like a duck then it's a duck.in other terms it means that we don't care what type of object we're dealing with we only care if it can do what we ask it to do.


class Duck:
    def quack(self):
        print("Quack, quack!")

    def fly(self):
        print("Flap, Flap!")


class Person:
    def qucak(self):
        print("I'm Quacking like a Duck!")

    def fly(self):
        print("I'm Flapping like a Duck!")


def quack_and_fly(thing):
    
    # NOT Duck_Typing (NON-PYTHONIC)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("This has to be a Duck!")


print()


d = Duck()

quack_and_fly(d)

p = Person()

quack_and_fly(p)
