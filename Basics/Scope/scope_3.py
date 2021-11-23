def outer_1():
    x = "outer1 x"

    def inner_1():
        x = "inner1 x"
        # this uses inner x local variable and does not refer to outer x enclosing variable
        print(x)

    inner_1()
    print(x)


outer_1()


def outer_2():
    x = "outer2 x"

    def inner_2():
        # now that there is no local x variable this uses the enclosing outer x variable
        print(x)

    inner_2()
    print(x)


outer_2()


def outer_3():
    x = "outer3 x"

    def inner_3():
        nonlocal x
        x = "outer x modified in inner_3 function"
        # nonlocal keyword refers to enclosing variables and modifies them instead of using a local variable
        # unlike global keyword the nonlocal keyword must be used on an existing enclosing varialbe and can't create a new one
        print(x)

    inner_3()
    print(x)


outer_3()
