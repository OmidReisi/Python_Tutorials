import curses
from curses import wrapper
import time


def main(main_window):
    main_window.clear()

    # you can create sub windows that are part of the main_window and take control of the cordinates of the main_window you give them
    # all the operations that you can do to a main_window you can do to sub windows as well
    # curses.newwin(rows, columns, start_row, start_column) takes at least 2 arguments (all 4 are positional arguments and the last 2 are optional) and returns a new window
    # rows represent number of rows(height) that this sub window controls from the main_window and columns specifies width of the sub window
    # start_row and start_column represent the upper_left_corner (starting position) of sub window in the main_window(the default value is always (0,0) even if there main_window or another sub window is occupying it)
    # if multiply windows collide with each other the last one is applied
    # the length of your text should always be smaller than the length of the window at least by one or an error is risen

    # when you create sub windows the cursor position does not change for the main window and continues were it left off (starting from (0,0))
    # main_window.addstr("main window")

    # it's best practice to refresh the main window before displaying sub windows
    main_window.refresh()

    sub_win_1 = curses.newwin(2, 10, 3, 5)
    sub_win_2 = curses.newwin(1, 10, 0, 0)
    sub_win_3 = curses.newwin(1, 10, 1, 0)

    sub_win_1.clear()
    # now that you're printing to the sub_win_1 the position you give to the string is relative to the sub_win_1 and not the main_window
    sub_win_1.addstr("this is 1")
    sub_win_1.refresh()
    # time.sleep(4)

    sub_win_2.clear()
    sub_win_2.addstr("this is 2")
    sub_win_2.refresh()

    sub_win_3.clear()
    sub_win_3.addstr("this is 3")
    sub_win_3.refresh()
    # time.sleep(4)

    # depending on the window you use the cursor is at the end of the text of that window (here it's on (0,0) of main window)
    main_window.getch()


wrapper(main)
