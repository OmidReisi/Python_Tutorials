import curses
from curses import wrapper
import time


def main(window):

    window.clear()

    # pad is somekind of abstract window that you can create and put text into it
    # curses.newpad(rows, columns) creates a new pad with the height of rows and width of columns
    # you can do evey operation that you do to a window to a pad as well
    my_pad = curses.newpad(100, 100)
    my_pad.clear()

    # always refresh your window after creating a new pad
    window.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(65 + j)
            my_pad.addstr(char)
    # when you want to refresh the pad it takes 6 arguments explained below (refresh(content_of_the_pad cordinates, content_display_starting_point, content_display_ending_point) note that these 3 each are representing 2 arguments that are all integers and are positional arguments)
    # content_of_the_pad cordinates: shows the upper_left_corner of the text you want to select from the pad (height (row) and width (column) respectively)
    # content_display_starting_point: shows the upper_left_corner of the rectangle you want to place your pad content into relative to the window( row and column respectively)
    # content_display_ending_point; shows the lower_right_corner of the rectangle you want to place your pad content into relative to the window (row and column respectively)
    # if your terminal size is smaller than the content you want to display then an error is risen
    my_pad.refresh(0, 0, 0, 0, 50, 50)
    window.getch()

    window.clear()
    window.refresh()

    # scroling the pad
    for i in range(50):
        my_pad.refresh(0, i, 10, 10, 25, 25)
        time.sleep(0.3)

    window.clear()
    window.refresh()

    # moving the pad_content up and down
    for i in range(20):
        my_pad.refresh(0, 0, i, 10, 10 + i, 20)
        time.sleep(0.3)

        window.clear()
        window.refresh()

    # moving the pad_content left and right
    for i in range(20):
        my_pad.refresh(0, 0, 10, i, 20, 10 + i)
        time.sleep(0.3)

        window.clear()
        window.refresh()

    # while moving pad content up and down or left and right (you can also do it diagonally) if you hit the end of the terminal from each side an error is risen
    # to get the size of your main_window use these two below
    # the -1 is for the amount of window you can use
    # always use this method in the main function that you pass to the wrapper
    window_size = (curses.LINES - 1, curses.COLS - 1)
    print(window_size)


wrapper(main)
