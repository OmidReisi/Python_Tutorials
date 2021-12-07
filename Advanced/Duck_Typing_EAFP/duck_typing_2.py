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

    # Duck_Typing (PYTHONIC)
    # this is Duck_Typing because the class person has quack and fly methods so it acts like a Duck and we don't check if it's actually a Duck or not.
    # Duck_Typing in this situation is dangerous because we don't know if our object has callable attributes "quack", "fly" so we have to check for their availablity without checking for the object's type

    thing.quack()
    thing.fly()

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
