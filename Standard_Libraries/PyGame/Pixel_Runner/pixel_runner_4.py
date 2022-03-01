from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

pygame.init()

screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()


sky_surface = pygame.image.load(r"./graphics/Sky.png")
ground_surface = pygame.image.load(r"./graphics/ground.png")

# in order to create a text surface in pygame first you need to define a Font object and then render that Font object to create a text surface.
# the first argument is the font type and the second one is the font size.
# the font type is just a path to a .ttf file(doesn't matter if it's installed or not)
# installed fonts are stored in c/windows/fonts
# if font type is set to None then the default font of pygame is used.
test_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

# the first argument is the text, the second one is antialiasing(AA) and the third argument is the color of the text
# antialiasing means the smoothing of the edges of the text.(always set this to True unless you're using pixel art and in this case we're using pixel art so we've set it to False)
# coloring works just like Surface.fill(color) and you can use RGB or RGBA or named colors.
# this render method returns a text surface and now we can place it on our display surface.
text_surface = test_font.render("My game", False, "Black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # note that these three surfaces are not static images and they're refreshing 60 times per second but because everytime they're set to the same position we see them as static images.
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)
