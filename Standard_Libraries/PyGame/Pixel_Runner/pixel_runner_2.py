from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

pygame.init()

# this is our display surface
screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()

# this is how you create a regular surface
# just like the display surface you need to pass a tuple of (width, height) to initiate the object
test_surface = pygame.Surface((Window_Size(width=100, height=200)))

# this is how we change the color of a Surface.
# you can use a tuple of RGB or RGBA values as well as the available named colors
# note that both display surface and regular surface are of type Surface therefore they share the same methods and attributes.
# test_surface.fill("white")
test_surface.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # this is how we connect a regular surface to the display surface.
    # the second argument is a tuple the shows the position that we want to put the regular surface on display surface(coords of top left corner)
    screen.blit(test_surface, (10, 0))

    pygame.display.update()
    clock.tick(60)
