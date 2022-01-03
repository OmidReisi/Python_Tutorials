# IDEMPOTENCE is used for expressions that do the same thing over and over again
# for example for functions if f(f(x)) = f(x) then this f functions is idempotent
# in general expressions in python are idempotent (a=10 this means that no matter how many times we run this it's always a=10)


def add_10(num):
    return num + 10


# this add_10 functions is not idempotent because the result_1 and result_2 dont' have the same value
result_1 = add_10(10)
result_2 = add_10(add_10(10))

print(result_1, result_2)


# the abs() function is idempotent
print(abs(-10))
print(abs(abs(-10)))


# HTTP METHODS GET, PUT, DELETE are idempotent but POST is not idempotent
