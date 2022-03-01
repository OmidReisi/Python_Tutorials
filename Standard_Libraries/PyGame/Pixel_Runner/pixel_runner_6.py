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

# in order to place surfaces exactly in the position we want them to be we use rectangles.
# .get_rect() method places a rectangle around our surface.
# giving coords to our rectangle is same as placing our surface on screen using blit and coords.
# you can use different positions of your rectangle to place on your screen the following are the available keyword arguments you can use for different coords for your rectangle:
# topleft, midtop, topright, midleft, center, midright, bottomleft, midbottom, bottomright
player_rect = player_surface.get_rect(midbottom=(80, 300))

snail_rect = snail_surface.get_rect(midbottom=(600, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, snail_rect)

    # screen.blit(player_surface, (80, 200))

    # this is same as the line above
    # now that we've defined a rectangle for our surface we place our rectangle on our screen which includes our surface as well.
    screen.blit(player_surface, player_rect)

    # you can use the same keyword arguments used to place a rectangle on the screen to move that rectangle.
    player_rect.left += 1

    snail_rect.right = (
        800 + snail_rect.width if snail_rect.right <= 0 else snail_rect.right - 4
    )

    # this method checks if two rectangles are colliding and return true if they are and false if they're not.
    if player_rect.colliderect(snail_rect):
        print("Collision detected!")

    pygame.display.update()
    clock.tick(60)
