from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()


# this is how we import an image and set it as a Surface
# this method returns a Surface object.
sky_surface = pygame.image.load(r"./graphics/Sky.png")
ground_surface = pygame.image.load(r"./graphics/ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # be careful not to overlapp two surfaces
    # if two surface are overlapped, then the first one stays hidden behind the second one.
    screen.blit(sky_surface, (0, 0))
    # note that our ground image height is 168px but because our display window has height of 400px then we don't see the remaining 68px of our groung image.
    screen.blit(ground_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)
