import random


# the way that random module works is that random numbers are not completely random and they are pesudo-random
# this means that they are generated by running some deterministic operations on the seed
# if the seed is constant and doesn't change value then every time you run your code you get the exact same result for random numbers.
# the default seed is the system time and that's why we get different results every time we run the program (the seed changes and the operations run on the seed generate different results)
# if you want to generate truely random numbers you have to use a truely random event (like the decay of the nukes or movement of the mouse) outside of your system as the source of your seed
# you can change the seed with this method below
random.seed(5)


# it's convention in python that if you want to create an unused variable you should use _ (underline) for it's name
for _ in range(10):

    # works like randint but the end is exclusive and you can pass a step as well
    # now that our seed is constant we get the exact same numbers evey time we run this program
    print(random.randrange(0, 10))