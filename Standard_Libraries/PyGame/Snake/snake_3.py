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

        # now we add graphics to our game
        self.fruit_surface: pygame.surface.Surface = pygame.image.load(
            r"./Graphics/apple.png"
        ).convert_alpha()

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
        screen.blit(self.fruit_surface, fruit_rect)


class Snake:
    def __init__(self) -> None:
        """initializing a snake with 3 blocks and setting it's default direction to the left."""

        self.body: list[Vector2] = [Vector2(14, 10), Vector2(15, 10), Vector2(16, 10)]

        self.head_up = pygame.image.load(r"Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load(r"Graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load(r"Graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load(r"Graphics/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(r"Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(r"Graphics/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(r"Graphics/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(r"Graphics/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(
            r"Graphics/body_vertical.png"
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            r"Graphics/body_horizontal.png"
        ).convert_alpha()

        self.body_tr = pygame.image.load(r"Graphics/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(r"Graphics/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(r"Graphics/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(r"Graphics/body_bl.png").convert_alpha()

        self.direction: Vector2 = Vector2(-1, 0)
        self.head_graphics: pygame.surface.Surface = self.head_left
        self.tail_graphics: pygame.surface.Surface = self.tail_right

    @property
    def head(self) -> Vector2:
        return self.body[0]

    @property
    def tail(self) -> Vector2:
        return self.body[-1]

    def draw(self, screen: pygame.surface.Surface) -> None:
        """drawing the snake on the given screen by drawing each block of the body

        Args:
            screen (pygame.surface.Surface): the screen to draw the snake blocks on.
        """

        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            block_rect: pygame.Rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            if block == self.head:
                screen.blit(self.head_graphics, block_rect)

            elif block == self.tail:
                screen.blit(self.tail_graphics, block_rect)

            else:
                previous_block_relation = self.body[index + 1] - block
                next_block_relation = self.body[index - 1] - block
                if previous_block_relation.x == next_block_relation.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block_relation.y == next_block_relation.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (
                        previous_block_relation.x == -1 and next_block_relation.y == -1
                    ) or (
                        previous_block_relation.y == -1 and next_block_relation.x == -1
                    ):
                        screen.blit(self.body_tl, block_rect)

                    elif (
                        previous_block_relation.x == -1 and next_block_relation.y == 1
                    ) or (
                        previous_block_relation.y == 1 and next_block_relation.x == -1
                    ):
                        screen.blit(self.body_bl, block_rect)

                    elif (
                        previous_block_relation.x == 1 and next_block_relation.y == -1
                    ) or (
                        previous_block_relation.y == -1 and next_block_relation.x == 1
                    ):
                        screen.blit(self.body_tr, block_rect)

                    elif (
                        previous_block_relation.x == 1 and next_block_relation.y == 1
                    ) or (
                        previous_block_relation.y == 1 and next_block_relation.x == 1
                    ):
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self) -> None:
        if self.head - self.body[1] == Vector2(-1, 0):
            self.head_graphics = self.head_left
        if self.head - self.body[1] == Vector2(1, 0):
            self.head_graphics = self.head_right
        if self.head - self.body[1] == Vector2(0, 1):
            self.head_graphics = self.head_down
        if self.head - self.body[1] == Vector2(0, -1):
            self.head_graphics = self.head_up

    def update_tail_graphics(self) -> None:
        direction: Vector2 = self.body[-2] - self.tail
        if direction == Vector2(-1, 0):
            self.tail_graphics = self.tail_right
        if direction == Vector2(1, 0):
            self.tail_graphics = self.tail_left
        if direction == Vector2(0, 1):
            self.tail_graphics = self.tail_up
        if direction == Vector2(0, -1):
            self.tail_graphics = self.tail_down

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
