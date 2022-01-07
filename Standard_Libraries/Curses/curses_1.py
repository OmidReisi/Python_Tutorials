# this module is used for having complete control over terminal and use coloring and styling it it (pip install windows-curses)
import curses
from curses import wrapper
import time

# if you want to use this function with wrapper(wrapper(main)) then it needs to accept at least one argument that represents the terminal.window (the name of this argument doesn't have to be stdscr it can be anything)
def main(terminal_window):

    # clears your terminal_window (always clear your terminal at the start)
    terminal_window.clear()

    # note that print() and input() funcion don't work on this terminal window because they print on the main terminal and terminal_windows is a winodw on top of the terminal
    # .addstr(r,c,str, [attr])
    # str is the string (CAN'T PASS BYTE OR INT) you want to print to the the terminal window
    # r, c are integers that represents the starting row=r , column=c of your string in terminal_window (these are optional and the default value is 0,0 ) (if there has been a .addstr() method before the next one continues from the position last one finished)
    # you can add other attributes as positional arguments (DON'T PASS THEM AS KEYWORD ARGUMENTS) to style your text (these are optional)
    terminal_window.addstr("Welcome to Python Curses Tutorials ...")

    # if multiple .addstr methods write to a same locations in terminal the last one overwrites them all
    terminal_window.addstr(0, 3, "Overwritten")

    # in order to print the text to terminal you have to use .refresh() (not using .refresh() only updates the virtual terminal)
    terminal_window.refresh()

    # this method waits until user hits a character on keyboard and returns the character
    terminal_window.getch()


# wrapper(func, *args, **kwargs) is a funcion that initializes a window terminal called stdscr and passes it to the func object as it's first argument
# args and kwargs are also passed to the func object following the stdscr argument
# the curses module actully initializes a window over your terminal and takes control of this window over your terminal
wrapper(main)
