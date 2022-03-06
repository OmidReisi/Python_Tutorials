from collections import namedtuple
from pygame.math import Vector2
import sys
import random
import pygame


class Fruit:
    def __init__(self) -> None:
        """initializing a fruit object with random position for drawing on the screen."""
        self.pos: Vector2 = Vector2(0, 0)
        self.new_block: Vector2 = Vector2(0, 0)
        self.randomize()

    def randomize(self) -> None:
        self.pos = Vector2(
            random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1)
        )

    def draw(self, screen: pygame.surface.Surface) -> None:
        """drawing the fruit block on the screen

        Args:
            screen (pygame.surface.Surface): the surface to draw the fruit on.
        """

        fruit_rect: pygame.Rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)


class Snake:
    def __init__(self) -> None:
        """initializing a snake with 3 blocks and setting it's default direction to the left."""

        self.body: list[Vector2] = [Vector2(14, 10), Vector2(15, 10), Vector2(16, 10)]

        self.direction: Vector2 = Vector2(-1, 0)

    @property
    def head(self) -> Vector2:
        return self.body[0]

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
        self.new_block = self.body.pop()

    def set_direction(self, key: int) -> None:
        """seting the direction of movement for the snake based on the input key

        Args:
            key (int): the input key received from event.key
        """
        match key:
            case pygame.K_UP if self.direction != Vector2(0, 1):
                self.direction = Vector2(0, -1)
            case pygame.K_DOWN if self.direction != Vector2(0, -1):
                self.direction = Vector2(0, 1)
            case pygame.K_LEFT if self.direction != Vector2(1, 0):
                self.direction = Vector2(-1, 0)
            case pygame.K_RIGHT if self.direction != Vector2(-1, 0):
                self.direction = Vector2(1, 0)

    def add_block(self) -> None:
        self.body.append(self.new_block)


# we create a main class for our game that contains both the fruit and the snake
# also with this main class it's easier to check for collision between our snake and fruit.
class MAIN:
    def __init__(self) -> None:
        self.snake: Snake = Snake()
        self.fruit: Fruit = Fruit()

    def draw(self, screen) -> None:
        self.fruit.draw(screen)
        self.snake.draw(screen)

    def update(self) -> None:
        self.snake.move()
        self.collision()
        self.check_fail()

    def collision(self) -> None:
        if self.fruit.pos == self.snake.head:
            self.snake.add_block()
            self.fruit.randomize()

    def check_fail(self) -> None:
        if (not 0 <= self.snake.head.x < CELL_NUMBER) or (
            not 0 <= self.snake.head.y < CELL_NUMBER
        ):
            self.game_over()

        if self.snake.head in self.snake.body[1:]:
            self.game_over()

    def game_over(self) -> None:
        pygame.quit()
        sys.exit()


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

    main_game: MAIN = MAIN()

    SNAKE_MOVEMENT: int = pygame.USEREVENT + 1
    pygame.time.set_timer(SNAKE_MOVEMENT, 150)

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                main_game.snake.set_direction(event.key)
            if event.type == SNAKE_MOVEMENT:
                main_game.update()

        main_win.fill(BG_COLOR)
        main_game.draw(main_win)

        pygame.display.update()
        clock.tick(60)


main()
