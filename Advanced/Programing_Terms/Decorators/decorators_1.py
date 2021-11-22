# A decorators is a function that takes another function as an argument and adds some kind of functionality then returns a function without altering the original input function


def decorator_fuction(original_function):
    def wrapper_function():
        print(f"Wrapper executed this before {original_function.__name__}")
        original_function()
        print(f"Wrapper executed this after {original_function.__name__}")

    return wrapper_function


# this line below is same as saying decorated_disply = decorator_function(disply)
# @decorator_fuction
def display():
    print("display function ran")


# same as @decorator_function
decorated_display = decorator_fuction(display)

decorated_display()
