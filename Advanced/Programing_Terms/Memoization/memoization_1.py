# memoization is the term we use for functions that store they return value of their calls with specific values in a memory_cache and then if the function is called again with same arguments insead of running the function again they return the value from the memory_cache
# memoization is very useful for recursive functions that take a lot of time to calculate

from functools import wraps


def factorial_decorator(original_func):
    @wraps(original_func)
    def wrapper_function(num):
        memory = {}
        if num not in memory:
            memory[num] = original_func(num)
        return memory[num]

    return wrapper_function


def timer_decorator(original_func):
    @wraps(original_func)
    def wrapper_function(num):
        import time

        t1 = time.time()
        result = original_func(num)
        t2 = time.time() - t1
        print("factorial({}) time elapsed: {} in seconds".format(num, t2))
        return result

    return wrapper_function


@timer_decorator
@factorial_decorator
def factorial(num):
    if num < 0:
        raise ValueError("factorial function works only for non-negative integers")
    # the raise error causes the control flow to be disrupted so it's better to use if instead of elif
    if num == 0:
        return 1
    # here again the return statement disrupts the control flow so no condition is needed
    return num * factorial(num - 1)


# running this function with factorial_decorator on and off shows that using memoization saves time in this function
result = factorial(5)
