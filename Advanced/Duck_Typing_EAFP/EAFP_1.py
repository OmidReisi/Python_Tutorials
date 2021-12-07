class Duck:
    def quack(self):
        print("Quack, quack!")

    def fly(self):
        print("Flap, Flap!")


class Person:
    def quack(self):
        print("I'm Quacking like a Duck!")

    def fly(self):
        print("I'm Flapping like a Duck!")


def quack_and_fly(thing):

    # this way of checking is called LBYL and is the NON-PYTHONIC way
    # LBYL : (Look Before You Leap) means that avoid errors by asking permissions first and is the non-pythonic way

    # hasattr is a built-in function that checks if a given object has the given name as attribute or not and returns a bool
    if hasattr(thing, "quack"):
        # callable is another built-in function that checks if a given object is callable or not(functions and classes are callables)
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, "fly"):
        if callable(thing.fly):
            thing.fly()

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
