import curses
from curses import wrapper


def main(window):
    window.clear()

    # curses.echo(True) shows the  input characters from the user in the terminal window
    # by default curse.echo(False) is set and we don't see the user input in the terminal
    curses.echo(True)
    while True:
        key = window.getkey()

        if key == "q":
            break


wrapper(main)
