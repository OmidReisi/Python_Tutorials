import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


def main(window):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    GREEN_AND_WHITE = curses.color_pair(1)

    window.clear()

    # with this method you can set and attribute for items that are between .attron() and .attroff() for that specific window
    window.attron(GREEN_AND_WHITE)
    # now the rectangle's border color is green and there is a white background for the rectangles border
    rectangle(window, 5, 5, 15, 15)
    # now everything that comes after this goes to back to normal colors
    window.attroff(GREEN_AND_WHITE)
    # after we turn off the attribute then this text is no longer in GREEN_AND_WHITE
    window.addstr(20, 20, "This text is white")

    # add a border around the whole window
    # you can change the border color with attron and attroff
    window.border()

    # move the curser to the given row and column relative to the screen
    window.move(10, 1)

    window.refresh()
    window.getkey()


wrapper(main)


# you can learn more on curses module at : https://docs.python.org/3.10/library/curses.html#module-curses
