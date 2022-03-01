from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])
RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()


sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

test_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

# you can use a tuple of 3 rgb values for coloring(R,G,B)
text_surface = test_font.render("My game", False, RGB_Color(64, 64, 64))

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

        if event.type == pygame.KEYDOWN:
            # note that you can only check for the type of the key only if a key is pressed.
            if event.key == pygame.K_SPACE:
                print("Jump!")

        if event.type == pygame.KEYUP:
            print("some key released!")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # you can use hexadecimal values for colors (#rrggbb)
    pygame.draw.rect(screen, "#c0e8ec", text_rect)
    pygame.draw.rect(screen, "#c0e8ec", text_rect, width=10)

    # pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), 5)
    # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

    screen.blit(text_surface, text_rect)
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_rect)

    # returns a sequence of bools for all the keyboard keys (true if the coresponding key is pressed else false)
    # using event loop for checking keys is better because in event loop we can differentiate between keys being pressed and keys being released.
    # k = pygame.key.get_pressed()
    # if k[pygame.K_SPACE]:
    #     print("Jump!")

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
