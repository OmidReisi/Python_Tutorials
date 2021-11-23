def square_numbers(nums):
    for num in nums:
        # yield keyword represents generators
        yield num * num


my_nums = square_numbers([1, 2, 3, 4, 5])

print(list(my_nums))

# converting the generator to a list is like running through so now it's empty
# print(next(my_nums))

# we can also create generators using comprehensions
new_nums = (n * n for n in [1, 2, 3, 4, 5])

# generators keep only one value at a time in memory and are much better in preformance than lists but they are not reverseable and you can't go back
print(list(new_nums))
