class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current_value = self.words[self.index]
            self.index += 1
            return current_value
        # raising exceptions from another exception is better to be this way
        except IndexError as e:
            raise StopIteration from e


my_sentence = Sentence("This is a test")

# for word in my_sentence:
#     print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))


def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentence("This is my generator test")

# for word in my_sentence:
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
