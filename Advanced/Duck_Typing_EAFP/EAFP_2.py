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

    # this way of handling checks is called EAFP and is the PYTHONIC-WAY
    # EAFP : (Easier to Ask Forgiveness than Permission)

    # here we do our work and if an error happens we handle it
    try:
        thing.quack()
        thing.fly()
        thing.bark()

    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
