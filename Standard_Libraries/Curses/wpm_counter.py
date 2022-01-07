import time
import random
import curses
from curses import wrapper

list_of_target_text = [
    "Hello world this is some test text for this app!",
    "Hi my name is Omid Reisi, I'm 21 years old and this app is working fine.",
    "I live in Mobarakeh, Isfahan and I study Computer Engineering.",
    "This is my last semester and after that I wil graduate from college.",
]


def start_screen(stdscr):

    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin ...")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target_text, current_text=None, WPM=0):

    if current_text is None:
        current_text = []

    stdscr.addstr(target_text)
    stdscr.addstr(1, 0, f"WPM: {WPM}")

    for index, char in enumerate(current_text):
        text_color_index = 1 if target_text[index] == char else 2
        stdscr.addstr(0, index, char, curses.color_pair(text_color_index))
    return current_text


def wpm_test(stdscr):
    target_text = random.choice(list_of_target_text)
    current_text = None
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        # first time we enter the while loop the elapsed time will be zero so we pass it for at least 1 second so we don't hit zero divion error in calculating WPM
        time_elapsed = max(time.time() - start_time, 1)
        current_text_length = len(current_text) if current_text is not None else 0
        WPM = round((current_text_length / (time_elapsed / 60)) / 5)

        stdscr.clear()
        current_text = display_text(stdscr, target_text, current_text, WPM)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue

        # 27 is the ordinal value of escape key
        if ord(key) == 27:
            break

        # in this system backspace is represented by "\b" but in other systems it might be one of the other two
        if key in {"KEY_BACKSPACE", "\b", "\x7f"}:
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:

        wpm_test(stdscr)
        stdscr.addstr(
            2,
            0,
            "Congragulation You've completed the test! Press Enter to restart the test or ESC to finish the test",
        )
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        else:
            continue


wrapper(main)
