for i in range(1, 11):
    # adding : in curly bracers represents the formating
    # :02 means add a 0 before number if it's a single digit(zero padding)
    # :03 meand add zeros if number is less than 3 digits
    sentence = "The value is {:02}".format(i)
    print(sentence)

pi = 3.14159265

# .2f says that round it up to 2 decimal points
# .3f says that round it up to 3 decimal points
sentence = "Pi is equal to {:.2f}".format(pi)
print(sentence)

# put , between each 3 digints
sentence = f"1 MB is equal to {1000**2:,} bytes"
print(sentence)

print()

# first comes the padding then , comes and then comes the decimal point
sentence = f"1 MB is equal to {1000**2:013,.2f} bytes"
print(sentence)
