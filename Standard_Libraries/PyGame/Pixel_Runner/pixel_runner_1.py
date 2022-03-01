from collections import namedtuple
import sys
import pygame

Window_Size = namedtuple("Window_Size", ["width", "height"])

# this initializes the pygame modules and must of their functionality depends on intialization. so you must use this line of code after importing pygame.
pygame.init()

# this returns a surface object which is basiclly the window that user will see when the program is ran.
# the set_mode() method takes a tuple of (width, height) for the screen size.(in pixels)
# this screen is shown to the user as long as the program is running
screen = pygame.display.set_mode(Window_Size(800, 400))

# this is the title shown on the window on the top left corner.if not set it's default title is "pygame window"
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()



while True:

    # gets the events from the event queue and removes them from the queue(returns a list of events)
    # an event is like a click of a button or a mouse movement.
    for event in pygame.event.get():

        # pygame.QUIT is the red x on top right side of the window that closes it.
        if event.type == pygame.QUIT:

            # this is like the opposite of pygame.init() and uninitializes pygame modules and after that you can't use any pygame attribute or module.
            pygame.quit()

            # the best way to terminate a program in production is using sys.exit()
            # you could also break out of the loop
            sys.exit()

    # this is how we update the screen we created with each iteration of the loop
    pygame.display.update()

    # this is how we set a maximum framerate for out game
    # this line here makes sure that this loop only runs maximum of 60 times in a second.
    # for simple 2d games you don't really need to set minimum framerate
    clock.tick(60)
