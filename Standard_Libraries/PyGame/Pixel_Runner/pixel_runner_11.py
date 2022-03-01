from collections import namedtuple
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


# there are a couple of ways to scale our surfaces in different sizes this is a simple one.
# pygame.transform.scale2x takes only one argument as the surface and doubles it's width and height.
# pygame.transform.rotozoom(surface,angle, scale) is considered one of the better trasform methods because, it keeps the aspect ratio the same and filters the image which smoothes it out and also can rotate it.
# pygame.transform submodule allows us to use different forms of transformations on our surfaces.

# player_stand = pygame.transform.scale(
#     pygame.image.load(r"./graphics/Player/player_stand.png"), (200, 400)
# ).convert_alpha()

player_stand = pygame.image.load(r"./graphics/Player/player_stand.png")
# angle(in degrees) rotates the surface anti-clock wise and scale is multiplies the width and height of the surface.
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

text_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

game_name = text_font.render("Pixel Runner", False, RGB_Color(111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = text_font.render("Press space to play", False, RGB_Color(111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -21

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        screen.blit(snail_surface, snail_rect)
        score = display_score()

        player_gravity = min(1000, player_gravity + 1)
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        snail_rect.right = (
            800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
        )

        if snail_rect.colliderect(player_rect):
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
