# in order to have decorators that accept arguments we should add another layer of decorator on top of our decorator_function


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed Before", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed After", original_function.__name__, "\n")
            return result

        return wrapper_function

    return decorator_function


# now we should use our prefix_decorator to pass an argument to it
@prefix_decorator("TESTING:")
def display_info(name, age):
    print(f"diplay_info ran with arguments ({name}, {age}")


display_info("John", 25)
display_info("Travis", 30)
