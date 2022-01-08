import curses
import random
from curses import wrapper


def screen_setup(screen, refresh_rate):
    screen.clear()
    screen.timeout(refresh_rate)
    curses.curs_set(False)
    screen.nodelay(True)
    screen.border()


def adding_snake(screen, snake):
    for part in snake:
        screen.addstr(part[0], part[1], "*")


def finding_food(snake, food_locations):
    food_available = food_locations.difference(snake)
    food = random.choice(list(food_available))
    return food


def adding_food(screen, food):
    screen.addstr(food[0], food[1], "#")


def main(screen):
    refresh_flag = True
    refresh_rate = 100
    screen_setup(screen, refresh_rate)
    window_height, window_width = screen.getmaxyx()

    head_x = window_width // 4
    head_y = window_height // 2

    snake = [
        (head_y, head_x),
        (head_y, head_x - 1),
        (head_y, head_x - 2),
        (head_y, head_x - 3),
        (head_y, head_x - 4),
    ]

    food_locations = {
        (food_y, food_x)
        for food_y in range(1, window_height - 1)
        for food_x in range(1, window_width - 1)
    }
    screen.addstr("Press any key to start the game ...")
    # for i in range(len(snake)):
    #     screen.addstr(snake[i][0], snake[i][1], "*")
    # screen.addstr(food[0], food[1], "+")
    food = finding_food(snake, food_locations)
    adding_food(screen, food)
    adding_snake(screen, snake)

    key = None
    while key == None:
        try:
            key = screen.getkey()
        except:
            pass

    key = "KEY_RIGHT"

    while True:
        previous_key = key

        try:
            key = screen.getkey()
        except:
            key = previous_key

        if key == "KEY_UP":
            head_y -= 1
        elif key == "KEY_DOWN":
            head_y += 1
        elif key == "KEY_RIGHT":
            head_x += 1
        elif key == "KEY_LEFT":
            head_x -= 1
        else:
            break
        if (head_y, head_x) in snake:
            break
        tail = snake.pop()
        snake.insert(0, (head_y, head_x))

        if snake[0][0] in [0, window_height] or snake[0][1] in [0, window_width]:
            break

        if snake[0] == food:
            refresh_flag = True
            snake.append(tail)
            food = finding_food(snake, food_locations)

        screen.clear()

        adding_snake(screen, snake)
        adding_food(screen, food)
        screen.addstr(1, 1, f"snake: {len(snake)}")
        if len(snake) % 7 == 0 and refresh_flag:
            screen.timeout(refresh_rate // 2)
            refresh_flag = False

        screen.border()


wrapper(main)
