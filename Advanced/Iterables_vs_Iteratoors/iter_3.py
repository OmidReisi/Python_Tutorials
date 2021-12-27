# generators are a form of iterators
# unlike classes we don't need to implement __iter__ and __next__ method ourselves and generators automatically do that
def my_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


nums = my_range(1, 10, 2)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
