# this is a new feature in python 3.10 that acts like a switch/case statement in other languages but also provides additional functionality.
# just like switch/case statement in other languages the first match that happens exits the match block.
x = "hey"

match x:
    case "hello":
        print("This is hello!")
    case "hi":
        print("This is hi!")

    # for the default case we use a underscore(_) which is also called the wildcard character and it's optional.
    case _:
        print("This is not hello or hi!")
