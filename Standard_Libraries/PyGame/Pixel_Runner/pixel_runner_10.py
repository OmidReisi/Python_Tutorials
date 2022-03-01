from collections import namedtuple
import sys
import pygame


def display_score():
    # this method returns an int showing the number of milliseconds passed since pygame.init() was called
    # in order to reset the timer when player loses we substrate the start_time form the time.get_ticks()
    current_time = pygame.time.get_ticks() - start_time
    score_surface = score_font.render(
        f"Score: {current_time//1000}", False, (64, 64, 64)
    )
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)
    screen.blit(score_surface, score_rect)


Window_Size = namedtuple("Window_Size", ["width", "height"])
RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

game_active = True

clock = pygame.time.Clock()
start_time = 0


sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

score_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)
# score_surface = score_font.render("My game", False, RGB_Color(64, 64, 64))

snail_surface = pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha()

player_surface = pygame.image.load(
    r"./graphics/Player/player_walk_1.png"
).convert_alpha()

player_rect = player_surface.get_rect(midbottom=(80, 300))

# we define a player gravity to implement the concept of falling and jumping.
player_gravity = 0

snail_rect = snail_surface.get_rect(midbottom=(600, 300))

# score_rect = score_surface.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -21

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # jumping is like giving a negative number to gravity then after the jump player falls right back down.
                    if player_rect.bottom >= 300:
                        player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 800
                # here we reset the timer so the score is set to 0 at the beginning of the game
                start_time = pygame.time.get_ticks()
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        screen.blit(snail_surface, snail_rect)
        display_score()

        # 1000 is just a threshold for player_gravity in case the player doesn't jump and we don't want to consume so much memory with a big number.
        player_gravity = min(1000, player_gravity + 1)
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # player_rect.left += 1
        snail_rect.right = (
            800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
        )

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("yellow")

    pygame.display.update()
    clock.tick(60)
