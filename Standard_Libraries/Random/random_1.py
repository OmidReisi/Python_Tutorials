# random should not be used for security purposes and secrets module is recommanded for that
import random

# random number between [0,1) (0 is inclusive but 1 is exclusive)
value = random.random()
print(value)


# return a random floating point number between the given range
value = random.uniform(1, 10)
print(value)

# return a random integer between given range (both inclusive)
value = random.randint(1, 6)
print(value)


greetings = ["Hello", "Hi", "Hey", "Hola", "Howdy"]


# returns a random value form a given sequence
random_greeting = random.choice(greetings)
print(random_greeting)


colors = ["Red", "Black", "Green"]


# returns a random k-length list from the given sequence
# weights is a sequence that represents the probablity of each element being selected in the main sequence(if None then all probablities are equal)
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

print()
print()

deck = list(range(1, 53))

print(deck)

print()
print()

# shuffles a list or any other mutable sequence in place (does not return a new list just changes the order of elements in a list)
random.shuffle(deck)
print(deck)

print()
print()

# like choices method but only selects unique elements
hand = random.sample(deck, k=5)
print(hand)
