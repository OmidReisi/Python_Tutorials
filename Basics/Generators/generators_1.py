def square_numbers(nums):
    for num in nums:
        # yield keyword represents generators
        yield num * num


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

# you can get the next item in a generator by using next function
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

# after we've gone through all items the generator throws a stop iteration error if we run through it again
# print(next(my_nums))
