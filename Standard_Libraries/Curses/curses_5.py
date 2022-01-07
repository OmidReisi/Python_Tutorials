import curses
from curses import wrapper


def main(window):
    window.clear()

    # this returns the ordinal value of the character input (if char="A" then this returns 65)
    # key = window.getch()

    # this returns the character itself from the input
    # you can pass a row and column to getkey() or getch() to position the cursor for input
    key = window.getkey()

    window.addstr(f"key: {key}")
    window.refresh()
    window.getkey()

    # if you set window.nodelay(True) then when we hit a getkey() or getch() method then it doesn't wait for the user to input a character
    # the default value for nodelay is False which means it waits for user indefinitely to enter something
    # when we set window.nodelay(True) it means that when we hit a getkey() or getch() method an error is risen so we need to handle it with try and except blocks
    window.nodelay(True)
    string_x = 0
    x, y = 0, 0
    while True:

        try:
            key = window.getkey()
        except:
            key = None

        if key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_LEFT":
            x -= 1

        window.clear()
        string_x += 1
        # this makes the string to move one square every 100 iteration of while loop (this is used to avoid time.sleep())
        # when window.nodelay(True) then this text moves on the window seperatly and doesn't wait for the user input
        window.addstr(0, string_x // 100, "hello world")

        # if we catch an user input then we move the cordinates around and our other text works seperatly(when window.nodelay(True))
        window.addstr(y, x, f"({y}, {x})")
        window.refresh()


wrapper(main)
