import curses
from curses import wrapper
import time


def main(stdscr):
    stdscr.clear()
    # you can attributes to a str by passing them as the last positional argument of the addstr method
    # you can add multiple attributes by piping them together (curses.A_UNDERLINE | curses.A_REVERSE)
    # depending on the system some attributes might not work properly
    # A_UNDERLINE, A_BOLD, A_REVERSE(reverses the foreground and background colors), A_BLINK(makes the text blinking) are some of the most useful attributes
    # full list of attributes: https://docs.python.org/3.10/library/curses.html?highlight=wrapper#constants
    REVERSE_COLOR = curses.A_REVERSE | curses.A_BOLD

    # in order to give color to our texts we first have to initialize a color pair with curses.init_pair()
    # curses.init_pair(pair_id, foreground_color, background_color) takes 3 arguments(all positional arguments) and initializes a color pair that can be used with it's pair_id (pair_id should be an integer that is greater that 0 (0 is reserved for black and white))
    # curses.init_pair() should always be used inside of the funcion that we pass to our wrapper
    # list of predefined colors: https://docs.python.org/3.10/library/curses.html?highlight=init_pair#constants
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)

    # after you create the color pair you can use them by passing the pair_id to curses.color_pair
    YELLOW_AND_BLUE = curses.color_pair(1)
    GREEN_AND_RED = curses.color_pair(2)
    # here we piping the color and reverse attribute so we see blue on yellow background
    stdscr.addstr("hello\n", REVERSE_COLOR | YELLOW_AND_BLUE)

    stdscr.addstr("hello")

    stdscr.refresh()
    stdscr.getch()

    for i in range(100):
        # if we don't clear the screen then each iteration adds to the end of the previous iteration
        stdscr.clear()

        color = YELLOW_AND_BLUE if i % 2 == 0 else GREEN_AND_RED
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)
