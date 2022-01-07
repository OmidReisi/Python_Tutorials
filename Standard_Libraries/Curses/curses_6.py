import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from typing import Text

# you can get input from the user with getkey and getch and store them in a list but for long inputs it's better to use Textboses


def main(window):
    window.clear()

    # rectangle is used to style your textbox with borders and has no functionality other than styling
    # rectangle (window, cordinate_top_left, cordinate_bottom_right) (5 total arguments and all of them are positional)
    # window: represents the window you want to draw the rectangle in
    # cordinate_top_left: row and column of the top left corner of the rectangle relative to the window
    # cordinate_bottom_right: row and column of the bottom left corner of the rectangle relative to the window
    # the default color of rectangle is white

    rectangle(window, 2, 2, 12, 22)
    window.refresh()
    window.getkey()

    # match the size and position of the window you want to set as textbox with the rectangle you want to use as border
    # in order to match the rectangle set the width and height of the window 1 less than the width and height of the rectangle (also add 1 to the starting position of the text)
    win_1 = curses.newwin(9, 19, 3, 3)

    # creates and returns a textbox on top of the given window
    box = Textbox(win_1)

    # you can start editing your textbox with this method
    # when you reach the end of the column of textbox it goes to the next line untill it reaches it' last row and then it doesn't catch anymore input
    # when you're done editing your text box press CTRL + G
    box.edit()

    # this returns the string of input text in the textbox(also catches the \n at the end of columns so you have to replace the "\n" with "")
    text = box.gather().strip().replace("\n", "")
    window.addstr(10, 40, text)
    window.refresh()
    window.getkey()


wrapper(main)
