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
text_surface = test_font.render("My game", False, "Black")

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

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("event collision!")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("any mouse button pressed!")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("any mouse button released!")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # with pygame.draw submodule you can draw different shapes on the screen.
    # for rectangles you have to specify the screen you want to draw on , the color of the rectangle, and the rectangle itself.
    # you can specify additional arguments like border radius and width of the border.
    # if you specify a width for your rectangle the inside of the rectangle with be empty.
    pygame.draw.rect(screen, "Pink", text_rect)
    # in order to fill the rectangle and have a width we need to draw it twice. once for the width and once for the fill
    pygame.draw.rect(screen, "Pink", text_rect, width=10)

    # this is how we draw a line
    pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), 5)
    # this is how we draw an ellipse that is bound within the rectangle we specify.
    # just like rectangle if we specify width inside of it will be empty.
    pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

    screen.blit(text_surface, text_rect)
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_rect)

    player_rect.left += 1

    snail_rect.right = (
        800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
    )

    # if player_rect.colliderect(snail_rect):
    #     print("Collision detected!")

    mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint(mouse_pos):

        print(pygame.mouse.get_pressed(5))

    pygame.display.update()
    clock.tick(60)
