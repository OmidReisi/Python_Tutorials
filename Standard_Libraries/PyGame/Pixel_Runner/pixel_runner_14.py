from collections import namedtuple
from random import randint, choice
from typing import Sequence
import sys
import pygame

# in order to make our program more robust, we use OOP to improve our objects.
# Sprite classes in pygame allow us to interact better with our game objects so it's always recommended to inherit from this class
# remember that for group.draw() to work the attributes name must be exactly "imgae" and "rect"
# now we can put all the functionality for the player in this class and clean up the code.
# you also need a update() method which is ran when we call group.update()
# in the update method we run all our other methods.
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.player_walk: Sequence[pygame.surface.Surface] = [
            pygame.image.load(r"./graphics/Player/player_walk_1.png").convert_alpha(),
            pygame.image.load(r"./graphics/Player/player_walk_2.png").convert_alpha(),
        ]
        self.player_jump: pygame.surface.Surface = pygame.image.load(
            r"./graphics/Player/jump.png"
        ).convert_alpha()
        self.player_index: float = 0

        self.image: pygame.surface.Surface = self.player_walk[self.player_index]
        self.rect: pygame.rect.Rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity: int = 0

    def apply_jump(self) -> None:
        keys: Sequence[bool] = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -21

    def apply_gravity(self) -> None:
        self.gravity = min(1000, self.gravity + 1)
        self.rect.bottom += self.gravity
        self.rect.bottom = min(self.rect.bottom, 300)

    def apply_animation(self) -> None:
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def reset_player(self) -> None:
        if not game_active:
            self.rect: pygame.rect.Rect = self.image.get_rect(midbottom=(80, 300))

    def update(self) -> None:
        if game_active:
            self.apply_jump()
            self.apply_gravity()
            self.apply_animation()
        else:
            self.reset_player()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type: str) -> None:
        super().__init__()
        self.type: str = type
        self.frames: Sequence = []
        self.y_pos: int = 0

        match self.type:
            case "fly":
                self.frames = [
                    pygame.image.load(r"./graphics/Fly/Fly1.png").convert_alpha(),
                    pygame.image.load(r"./graphics/Fly/Fly2.png").convert_alpha(),
                ]
                self.y_pos = 200
            case "snail":
                self.frames = [
                    pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha(),
                    pygame.image.load(r"./graphics/snail/snail2.png").convert_alpha(),
                ]
                self.y_pos = 300
            case _:
                raise ValueError("Obstacle.type must of type ('fly'|'snail')")
        self.animation_index: float = 0

        self.image: pygame.surface.Surface = self.frames[self.animation_index]
        self.rect: pygame.rect.Rect = self.image.get_rect(
            midbottom=(randint(900, 1200), self.y_pos)
        )

    def apply_animation(self) -> None:
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self) -> None:
        if self.rect.right < 0:
            # this method removes the sprite from all the Groups
            self.kill()

    def update(self) -> None:
        self.rect.right -= 6
        self.apply_animation()
        self.destroy()


def display_score() -> int:
    current_time: int = pygame.time.get_ticks() - start_time
    score_surface: pygame.surface.Surface = text_font.render(
        f"Score: {current_time//1000}", False, (64, 64, 64)
    )
    score_rect: pygame.rect.Rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)
    screen.blit(score_surface, score_rect)

    return current_time // 1000


def collision_sprite() -> bool:
    # this is how we check for a collision between a sprite and a group
    # the bool argument destroys the sprite in group if collision has happened.
    if pygame.sprite.spritecollide(player_group.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


Window_Size = namedtuple("Window_Size", ["width", "height"])
RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

pygame.init()
screen: pygame.surface.Surface = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock: pygame.time.Clock = pygame.time.Clock()
start_time: int = 0
score: int = 0
game_active: bool = False

# in order to show Sprite objects on the screen we need to add them to a group
# there are two types of groups in pygame.sprit:    1.GroupSingle  2.Group
# GroupSingle can only hold 1 sprite at a time (the last one that is added)
# Group can hold multiple sprites.
# for our player we use GroupSingle because there's only 1 player
# for our snails and flys we use Group because we have more than one of them
# if you need to check for collision of two Sprites they need to be in different Groups.
player_group: pygame.sprite.GroupSingle = pygame.sprite.GroupSingle()
# we add our player sprite to the Player Group.
player_group.add(Player())

obstacle_group: pygame.sprite.Group = pygame.sprite.Group()

sky_surface: pygame.surface.Surface = pygame.image.load(
    r"./graphics/Sky.png"
).convert_alpha()
ground_surface: pygame.surface.Surface = pygame.image.load(
    r"./graphics/ground.png"
).convert_alpha()


player_stand: pygame.surface.Surface = pygame.image.load(
    r"./graphics/Player/player_stand.png"
)
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect: pygame.rect.Rect = player_stand.get_rect(center=(400, 200))

text_font: pygame.font.Font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

game_name: pygame.surface.Surface = text_font.render(
    "Pixel Runner", False, RGB_Color(111, 196, 169)
)
game_name_rect: pygame.rect.Rect = game_name.get_rect(center=(400, 80))

game_message: pygame.surface.Surface = text_font.render(
    "Press space to play", False, RGB_Color(111, 196, 169)
)
game_message_rect = game_message.get_rect(center=(400, 350))

obstacle_timer: int = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # in order to show a group on the screen we need to draw it.
        player_group.draw(screen)
        # this calls the update method of every sprite member
        player_group.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        screen.fill(RGB_Color(94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        score_message = text_font.render(
            f"Your score: {score}", False, RGB_Color(111, 196, 169)
        )
        score_message_rect = score_message.get_rect(center=(400, 350))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        player_group.update()

    pygame.display.update()
    clock.tick(60)
