def square_numbers(nums):
    for num in nums:
        # yield keyword represents generators
        yield num * num


my_nums = square_numbers([1, 2, 3, 4, 5])

# we can go through generators with for loops as well
# for loops know when a generator is out of item and stops so no exception is thrown
for num in my_nums:
    print(num)

