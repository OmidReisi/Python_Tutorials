from collections import deque


# deque (pronounced deck) is just like a list with some extra features
# if you want to access items in the beginning or the ending it's better to use deque instead of a list.

# you can specify a maxlen that can only be set when constructing a deque
# if you set a max len when adding items to the deque if you add more than maxlen removes items from the beginning of the deque.
d_1 = deque([1, 2, 3, 4], maxlen=6)

# adds an iterable to end of the deque
d_1.extend([1, 2, 3, 4, 5])
print(d_1)

# can't change the maxlen after the deque has been created.
# d_1.maxlen = 9

# adds to the beginning of the deque
# adds the iterable from right to left(last item becomes the first item in the deque)
d_1.extendleft("hey")
print(d_1)

# removes and returns the last item
print(d_1.pop())

# removes and returns the first item
print(d_1.popleft())

print(d_1)

# adds the item to the end of the deque
d_1.append("l")

# adds the item to the beginning of the deque
d_1.appendleft("f")

print(d_1)

d_2 = deque("hey")

# moves each item in the deque backward( if a negative number is passed) or forward (if a positive number is passed) by the value of number
# when reaches end or the beginning of the deque goes to the opposite side.
d_2.rotate(-1)
print(d_2)
