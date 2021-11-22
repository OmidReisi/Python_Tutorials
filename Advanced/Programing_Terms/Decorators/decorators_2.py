# this is not recommended it is best practice to use wrapper functions in decorator_functions and return the wrapper funcion
# one problem with not using wrapper is that you can't decorate after you return your original funcion
def decorator_func(original_func):
    print("no wrapper just execute {}".format(original_func.__name__))
    return original_func


@decorator_func
def display():
    print("display function")


display()
