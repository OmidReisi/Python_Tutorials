def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func()


# Closure is an inner function that remembers and has access to variables in local scope in which it was created even after the outer function is finished executing
outer_func()
