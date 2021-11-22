# to implement class decorators we initiate the original function in __init__ method and the __call__ mehtod is the equivalent of wrapper function
# both class_decorators and function_decorators are used (function_decorator is more common)
# it is best practice to use class_decorators for decorators that do a lot of work and function_decorators for decorators with less work


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        self.original_function(*args, **kwargs)
        print(
            f"call method executed this after {self.original_function.__name__}",
            end="\n\n",
        )


@decorator_class
def display():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info("John", 25)
display()
