from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()


sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

test_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)
text_surface = test_font.render("My game", False, "Black").convert()

snail_surface = pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha()

player_surface = pygame.image.load(
    r"./graphics/Player/player_walk_1.png"
).convert_alpha()

player_rect = player_surface.get_rect(midbottom=(80, 300))

snail_rect = snail_surface.get_rect(midbottom=(600, 300))

text_rect = text_surface.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # this is another way of getting the mouse position
        # remember that pygame.MOUSEMOTION is only true if mouse is moving and it's not static
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("event collision!")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("any mouse button pressed!")
        if event.type == pygame.MOUSEBUTTONUP:
            print("any mouse button released!")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, text_rect)
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_rect)

    player_rect.left += 1

    snail_rect.right = (
        800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
    )

    # if player_rect.colliderect(snail_rect):
    #     print("Collision detected!")

    # this method returns a tuple of mouse position on the screen
    mouse_pos = pygame.mouse.get_pos()

    # this method checks if our rectangle collides with a point on the screen.
    # you can pass a tuple or two individual numbers for coords.
    if player_rect.collidepoint(mouse_pos):

        # returns a tuple of 3 or 5 (based on the given number of mouse keys) that show true or false for different mouse buttons.
        print(pygame.mouse.get_pressed(5))

    pygame.display.update()
    clock.tick(60)
