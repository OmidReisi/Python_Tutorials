import sys
from typing import Literal
from collections import namedtuple

import pygame

pygame.init()

RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

WHITE = RGB_Color(255, 255, 255)
BLACK = RGB_Color(0, 0, 0)
LIGHT_GRAY = RGB_Color(120, 120, 120)

Point = namedtuple("Point", ["x", "y"])

Window_Size = namedtuple("Window_Size", ["Width", "Height"])

WIN_SIZE = Window_Size(700, 500)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 10


WINNING_SCORE = 5
SCORE_FONT = pygame.font.SysFont("comicsans", 40)


class Paddle:

    COLOR = WHITE
    VELOCITY = 0.7

    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw(self, win: pygame.Surface):
        self.rect = pygame.draw.rect(
            win, self.COLOR, (self.x_pos, self.y_pos, self.width, self.height)
        )

    def move(self, direction: Literal["up", "down"]):
        if direction == "up":
            self.y_pos = (
                self.y_pos - self.VELOCITY if self.y_pos >= self.VELOCITY else 0
            )
        elif direction == "down":
            self.y_pos = (
                self.y_pos + self.VELOCITY
                if self.y_pos <= WIN_SIZE.Height - PADDLE_HEIGHT - self.VELOCITY
                else WIN_SIZE.Height - PADDLE_HEIGHT
            )


class Ball:

    COLOR = WHITE
    MAX_VEL = 0.4

    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win: pygame.Surface):
        self.rect = pygame.draw.circle(win, self.COLOR, self.center, self.radius)

    def move(self):

        x_pos = self.center.x + self.x_vel
        y_pos = self.center.y + self.y_vel

        self.center = Point(x_pos, y_pos)


def draw(
    win: pygame.Surface, paddles: list[Paddle], ball: Ball, left_score, right_score
):

    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.draw.line(
        win,
        LIGHT_GRAY,
        (WIN_SIZE.Width // 2, 0),
        (WIN_SIZE.Width // 2, WIN_SIZE.Height),
        width=10,
    )

    left_score_text = SCORE_FONT.render(str(left_score), True, LIGHT_GRAY)
    right_score_text = SCORE_FONT.render(str(right_score), True, LIGHT_GRAY)

    left_score_rect = left_score_text.get_rect(center=(WIN_SIZE.Width // 4, 40))
    right_score_rect = right_score_text.get_rect(center=(3 * WIN_SIZE.Width // 4, 40))

    win.blit(left_score_text, left_score_rect)
    win.blit(right_score_text, right_score_rect)

    ball.draw(win)

    pygame.display.update()


def paddle_movement(keys, right_paddle: Paddle, left_paddle: Paddle):
    if keys[pygame.K_UP]:
        right_paddle.move("up")
    if keys[pygame.K_DOWN]:
        right_paddle.move("down")
    if keys[pygame.K_w]:
        left_paddle.move("up")
    if keys[pygame.K_s]:
        left_paddle.move("down")


def collision(ball: Ball, right_paddle: Paddle, left_paddle: Paddle):

    if ball.center.y + ball.radius >= WIN_SIZE.Height:
        ball.y_vel *= -1

    elif ball.center.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel > 0 and ball.rect.colliderect(right_paddle.rect):
        ball.x_vel *= -1
        ball.y_vel = trajectory_vel(ball, right_paddle)

    elif ball.x_vel < 0 and ball.rect.colliderect(left_paddle.rect):
        ball.x_vel *= -1
        ball.y_vel = trajectory_vel(ball, left_paddle)


def trajectory_vel(ball: Ball, paddle: Paddle):

    MAX_DISTANCE = PADDLE_HEIGHT // 2 + BALL_RADIUS
    distance = ball.rect.center[1] - paddle.rect.center[1]

    return ball.MAX_VEL * distance / MAX_DISTANCE


def reset(ball: Ball):
    ball.center = Point(WIN_SIZE.Width // 2, WIN_SIZE.Height // 2)
    ball.y_vel = 0


def main():

    WIN = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption("Pong")
    run = True
    clock = pygame.time.Clock()

    left_score = 0
    right_score = 0

    left_paddle = Paddle(
        10, WIN_SIZE.Height // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
    )

    right_paddle = Paddle(
        WIN_SIZE.Width - PADDLE_WIDTH - 10,
        WIN_SIZE.Height // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    ball = Ball(Point(WIN_SIZE.Width // 2, WIN_SIZE.Height // 2), BALL_RADIUS)

    while run:

        clock.tick()
        draw(WIN, [right_paddle, left_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        paddle_movement(keys, right_paddle, left_paddle)

        ball.move()
        collision(ball, right_paddle, left_paddle)

        if ball.center.x < 0:
            right_score += 1
            reset(ball)
        elif ball.center.x > WIN_SIZE.Width:
            left_score += 1
            reset(ball)

        if left_score == WINNING_SCORE or right_score == WINNING_SCORE:

            winner = "Left" if left_score == WINNING_SCORE else "Right"
            game_message_text = SCORE_FONT.render("Game Over", True, LIGHT_GRAY)

            game_message_rect = game_message_text.get_rect(
                center=(WIN_SIZE.Width // 2, WIN_SIZE.Height // 2)
            )
            game_score_text = SCORE_FONT.render(
                f"{winner} Player wins", True, LIGHT_GRAY
            )
            game_score_rect = game_score_text.get_rect(
                midtop=game_message_rect.midbottom
            )
            WIN.fill(WHITE)
            WIN.blit(game_message_text, game_message_rect)
            WIN.blit(game_score_text, game_score_rect)
            pygame.display.update()

            pygame.time.delay(3000)

            left_score = 0
            right_score = 0

            left_paddle.x_pos = 10
            left_paddle.y_pos = WIN_SIZE.Height // 2 - PADDLE_HEIGHT // 2
            right_paddle.x_pos = WIN_SIZE.Width - PADDLE_WIDTH - 10
            right_paddle.y_pos = WIN_SIZE.Height // 2 - PADDLE_HEIGHT // 2


if __name__ == "__main__":
    main()
