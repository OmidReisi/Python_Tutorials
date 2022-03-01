from collections import namedtuple
from random import randint
import sys
import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = text_font.render(
        f"Score: {current_time//1000}", False, (64, 64, 64)
    )
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)
    screen.blit(score_surface, score_rect)

    return current_time // 1000


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            obstacle.right -= 5
            screen.blit(snail_surface, obstacle)

        return [obstacle for obstacle in obstacle_list if obstacle.right > 0]
    else:
        return []


Window_Size = namedtuple("Window_Size", ["width", "height"])
RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

pygame.init()
screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()
start_time = 0
score = 0
game_active = False

sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

snail_surface = pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load(
    r"./graphics/Player/player_walk_1.png"
).convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

player_stand = pygame.image.load(r"./graphics/Player/player_stand.png")
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

text_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

game_name = text_font.render("Pixel Runner", False, RGB_Color(111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = text_font.render("Press space to play", False, RGB_Color(111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 350))

# in order to use timers in pygame you need to create a custom user event and then call that event in certain time intervals.
# this is how we create new custom user events.(always use +1 or +2 or ... and never use the default USEREVENT)
obstacle_timer = pygame.USEREVENT + 1
# this is how trigger a User Event in pygame(pygame.time.set_timer(event,milliseconds))
pygame.time.set_timer(obstacle_timer, 1500)

# now we want to generate a list of obstacles that just keep comming in each obstacle_timer interval
obstacle_rect_list = [snail_rect]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -21

            # now that we're triggring our event every 1500 milliseconds, we catch this event in our event loop.
            if event.type == obstacle_timer:
                # every 1500 milliseconds we're adding a new obstacle to the list with random starting position.
                obstacle_rect_list.append(
                    snail_surface.get_rect(midbottom=(randint(900, 1200), 300))
                )

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 800
                obstacle_rect_list = [snail_rect]
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        score = display_score()

        player_gravity = min(1000, player_gravity + 1)
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # snail_rect.right = (
        #     800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
        # )
        for obstacle_rect in obstacle_rect_list:
            if obstacle_rect.colliderect(player_rect):
                game_active = False
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

    pygame.display.update()
    clock.tick(60)
