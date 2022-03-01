from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()


# convert and convert_alpha methods converts our Surfaces and can be used to change their pixel format.(if no argument is passed uses the display surface format for them)
# use convert for images with mode RGB and convert_alpha for images with mode RGBA.
# using convert and convert_alpha methods increases performance of pygame.
sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

test_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)
text_surface = test_font.render("My game", False, "Black").convert()

snail_surface = pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha()

snail_x_pos = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 264))

    # we move the snail 1px to the left every frame.
    # when the snail reaches the left side we reset it at the right side.
    snail_x_pos = 795 if snail_x_pos < -65 else snail_x_pos - 4

    # note that if we remove all the other surfaces we see that the snail's previous frame is shown on the display so it's important to have a background so that background is shown over those previous frames.

    pygame.display.update()
    clock.tick(60)
