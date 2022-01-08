import curses
from curses import wrapper


def main(window):
    window.clear()

    # window.timeout(refresh_rate) refreshes the screen every refresh_rate (in milliseconds) so you don't have to use window.refresh()

    # you can turn off the cursor on the terminal with this method(default is curses.curs_set(True))
    curses.curs_set(False)
    # curses.echo(True) shows the  input characters from the user in the terminal window
    # by default curse.echo(False) is set and we don't see the user input in the terminal
    curses.echo(True)
    while True:
        key = window.getkey()

        if key == "q":
            break


wrapper(main)
