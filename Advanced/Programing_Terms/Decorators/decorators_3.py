def decorator_fuction(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        original_function(*args, **kwargs)
        print(f"Wrapper executed this after {original_function.__name__}", end="\n\n")

    return wrapper_function


@decorator_fuction
def display():
    print("display function ran")


@decorator_fuction
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info("John", 25)
display()
