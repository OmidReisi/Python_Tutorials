from collections import namedtuple
from pygame.math import Vector2
import sys
import random
import pygame


class Fruit:
    def __init__(self) -> None:
        """initializing a fruit object with random position for drawing on the screen."""

        # for doing vector and matrix operations we use vector and make it easier than using list or tuples.
        self.pos: Vector2 = Vector2(
            random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1)
        )

    def draw(self, screen: pygame.surface.Surface) -> None:
        """drawing the fruit block on the screen

        Args:
            screen (pygame.surface.Surface): the surface to draw the fruit on.
        """

        # you can access vector values like attributes with "."
        fruit_rect: pygame.Rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)


class Snake:
    def __init__(self) -> None:
        """initializing a snake with 3 blocks and setting it's default direction to the left."""

        self.body: list[Vector2] = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

        self.direction: Vector2 = Vector2(-1, 0)

    def draw(self, screen: pygame.surface.Surface) -> None:
        """drawing the snake on the given screen by drawing each block of the body

        Args:
            screen (pygame.surface.Surface): the screen to draw the snake blocks on.
        """
        for block in self.body:
            block_rect: pygame.Rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(screen, SNAKE_COLOR, block_rect)

    def move(self) -> None:
        """moving the snake based on it's direction."""

        self.body.insert(0, self.body[0] + self.direction)
        self.body.pop()

    def set_direction(self, key: int) -> None:
        """seting the direction of movement for the snake based on the input key

        Args:
            key (int): the input key received from event.key
        """
        match key:
            case pygame.K_UP:
                self.direction = Vector2(0, -1)
            case pygame.K_DOWN:
                self.direction = Vector2(0, 1)
            case pygame.K_LEFT:
                self.direction = Vector2(-1, 0)
            case pygame.K_RIGHT:
                self.direction = Vector2(1, 0)


RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

BG_COLOR: RGB_Color = RGB_Color(209, 192, 180)
FRUIT_COLOR: RGB_Color = RGB_Color(126, 166, 114)
SNAKE_COLOR: RGB_Color = RGB_Color(82, 12, 32)

# for the snake game our window needs to be like a grid and we need a flexible screen for that.
CELL_SIZE: int = 40
CELL_NUMBER: int = 20

main_win: pygame.surface.Surface = pygame.display.set_mode(
    (CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER)
)
pygame.display.set_caption("Snake Game")


def main() -> None:
    RUN: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()

    fruit = Fruit()
    snake = Snake()

    SNAKE_MOVEMENT: int = pygame.USEREVENT + 1
    pygame.time.set_timer(SNAKE_MOVEMENT, 150)

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.set_direction(event.key)
            if event.type == SNAKE_MOVEMENT:
                snake.move()

        main_win.fill(BG_COLOR)
        snake.draw(main_win)
        fruit.draw(main_win)

        pygame.display.update()
        clock.tick(60)


main()
