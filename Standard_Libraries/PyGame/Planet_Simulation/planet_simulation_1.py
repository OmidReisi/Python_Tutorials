from collections import namedtuple
import sys
import math
import pygame


RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

WHITE: RGB_Color = RGB_Color(255, 255, 255)
GREEN: RGB_Color = RGB_Color(0, 255, 0)
YELLOW: RGB_Color = RGB_Color(255, 255, 0)
LIGHT_BLUE: RGB_Color = RGB_Color(100, 149, 237)

WIDTH: int = 800
HEIGHT: int = 800


# class Circle(pygame.sprite.Sprite):
#     def __init__(
#         self, Color: tuple[int, int, int], radius: int, pos: tuple[int, int]
#     ) -> None:
#         super().__init__()

#         self.color = Color
#         self.radius = radius
#         self.pos = pos

#         # this is how we draw different shapes with sprites.
#         self.image = pygame.Surface((self.radius * 2, self.radius * 2))
#         # self.image.fill(WHITE)
#         pygame.draw.circle(
#             self.image, self.color, (self.radius, self.radius), self.radius
#         )
#         self.rect = self.image.get_rect(center=self.pos)


class Planet:

    # Astronomical unit (distance of earth from the sun in meters).
    AU: float = 149.6e6 * 1000

    # Constant of Gravitation
    G: float = 6.67428e-11

    # 1 AU = 100 px
    SCALE: float = 250 / AU

    # timestep for each frame (each frame shows the planet simulation after 1 day of the previous frame).
    TIMESTEP: int = 3600 * 24

    def __init__(
        self,
        color: tuple[int, int, int],
        radius: int,
        pos: tuple[float, float],
        mass: float,
    ) -> None:
        """for creating a Planet with the given color, radius. also defining self.x_vel and self.y_vel for the velocity of the planet movement.

        Args:
            color (tuple[int, int]): the color of the planet
            radius (int): the radius of the planet
            pos (tuple[int, int]): the position for the planet to place on the screen
            mass (int): weight of the planet in (kg)
        """
        self.color: tuple[int, int, int] = color
        self.radius: int = radius
        self.pos: tuple[float, float] = pos
        self.mass: float = mass

        self.IS_SUN: bool = False
        self.distance_to_sun: bool = False
        self.x_vel: int = 0
        self.y_vel: int = 0

    def draw(self, screen: pygame.surface.Surface) -> None:
        x_pos: float = self.pos[0] * self.SCALE + WIDTH / 2
        y_pos: float = self.pos[1] * self.SCALE + HEIGHT / 2

        pygame.draw.circle(screen, self.color, (x_pos, y_pos), self.radius)


pygame.init()

main_win: pygame.surface.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulator")

# circle = pygame.sprite.Group()
# circle.add(Circle(GREEN, 200, (400, 400)))


def main():
    run: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()

    sun: Planet = Planet(YELLOW, 30, (0, 0), 1.98892e30)
    sun.IS_SUN = True

    earth: Planet = Planet(LIGHT_BLUE, 16, (-1 * Planet.AU, 0), 5.9742e24)

    planets: list[Planet] = [sun, earth]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        for planet in planets:
            planet.draw(main_win)

        # circle.draw(main_win)

        pygame.display.update()
        clock.tick(60)


main()
