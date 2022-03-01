from __future__ import annotations
from collections import namedtuple
import sys
import math
import pygame


RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

BLACK: RGB_Color = RGB_Color(0, 0, 0)
WHITE: RGB_Color = RGB_Color(255, 255, 255)
DARK_GREEN: RGB_Color = RGB_Color(0, 150, 0)
YELLOW: RGB_Color = RGB_Color(255, 255, 0)
LIGHT_BLUE: RGB_Color = RGB_Color(100, 149, 237)
RED: RGB_Color = RGB_Color(188, 39, 50)
DARK_GRAY: RGB_Color = RGB_Color(80, 71, 81)

WIDTH: int = 800
HEIGHT: int = 800


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
        name: str,
        color: tuple[int, int, int],
        radius: int,
        pos: tuple[float, float],
        mass: float,
    ) -> None:
        """for creating a Planet with the given name,color, radius. also defining self.x_vel and self.y_vel for the velocity of the planet movement.

        Args:
            color (tuple[int, int]): the color of the planet
            radius (int): the radius of the planet
            pos (tuple[int, int]): the position for the planet to place on the screen
            mass (int): weight of the planet in (kg)
        """
        self.name: str = name
        self.color: tuple[int, int, int] = color
        self.radius: int = radius
        self.pos: tuple[float, float] = pos
        self.mass: float = mass

        # this is a list of positions that the planet has crossed in order to get orbit of the planet.
        self.orbit: list[tuple[float, float]] = []
        self.IS_SUN: bool = False
        self.distance_to_sun: float = 0
        self.x_vel: float = 0
        self.y_vel: float = 0

    def draw(self, screen: pygame.surface.Surface) -> None:
        """for drawing the planet on the screen

        Args:
            screen (pygame.surface.Surface): the surface used for drawing the planet
        """
        x_pos: float = self.pos[0] * self.SCALE + WIDTH / 2
        y_pos: float = self.pos[1] * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points: list[tuple[float, float]] = []
            for point in self.orbit:
                x: float = point[0] * self.SCALE + WIDTH / 2
                y: float = point[1] * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            # this draws a line between a sequence of points
            # the bool is if the line has an endpoint (enclosing line)
            pygame.draw.lines(screen, self.color, False, updated_points, 2)
        pygame.draw.circle(screen, self.color, (x_pos, y_pos), self.radius)

        if not self.IS_SUN:
            distance_surface: pygame.surface.Surface = text_font.render(
                f"{self.name}: {round(self.distance_to_sun/1000,1)}km", True, DARK_GREEN
            )
            distance_rect: pygame.rect.Rect = distance_surface.get_rect(
                center=(x_pos, y_pos)
            )
            screen.blit(distance_surface, distance_rect)
        else:
            text_surface: pygame.surface.Surface = text_font.render(
                f"{self.name}", True, DARK_GREEN
            )
            text_rect: pygame.rect.Rect = text_surface.get_rect(center=(x_pos, y_pos))
            screen.blit(text_surface, text_rect)

    def attraction_force(self, other: Planet) -> tuple[float, float]:
        """for calculating the force of attraction between two planets and calculating this force in x,y axis.

        Args:
            other (Planet): the planet used for calculating the force with this planet

        Returns:
            tuple[float, float]: a tuple of (force_x, force_y)
        """
        distance_x: float = other.pos[0] - self.pos[0]
        distance_y: float = other.pos[1] - self.pos[1]
        distance: float = math.sqrt(distance_x**2 + distance_y**2)

        if other.IS_SUN:
            self.distance_to_sun = distance

        force: float = self.G * self.mass * other.mass / distance**2
        theta_angle: float = math.atan2(distance_y, distance_x)
        force_x: float = math.cos(theta_angle) * force
        force_y: float = math.sin(theta_angle) * force
        return force_x, force_y

    def update_position(self, planets: list[Planet]) -> None:
        """for updating positions of each planet by calculating the velocity of planet based on the force of attraction of all other planets.

        Args:
            planets (list[Planet]): list of all planets that affect the force of attraction and velocity of this planet
        """
        total_force_x = sum(
            [
                self.attraction_force(planet)[0]
                for planet in planets
                if self is not planet
            ]
        )
        total_force_y = sum(
            [
                self.attraction_force(planet)[1]
                for planet in planets
                if self is not planet
            ]
        )

        self.x_vel += (total_force_x / self.mass) * self.TIMESTEP
        self.y_vel += (total_force_y / self.mass) * self.TIMESTEP

        self.pos = (
            self.pos[0] + self.x_vel * self.TIMESTEP,
            self.pos[1] + self.y_vel * self.TIMESTEP,
        )
        self.orbit.append(self.pos)


pygame.init()

main_win: pygame.surface.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulator")

text_font: pygame.font.Font = pygame.font.SysFont("Comic Sans MS", 20)


def main():
    run: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()

    sun: Planet = Planet("SUN", YELLOW, 30, (0, 0), 1.98892e30)
    sun.IS_SUN = True

    earth: Planet = Planet("EARTH", LIGHT_BLUE, 16, (-1 * Planet.AU, 0), 5.9742e24)
    # if there was no y_vel for the planets the only velocity would be the force of attraction they would just be absorbed by the sun.
    earth.y_vel = 29.783e3

    mars: Planet = Planet("MARS", RED, 12, (-1.524 * Planet.AU, 0), 6.39e23)
    mars.y_vel = 24.077e3

    mercury: Planet = Planet("MERCURY", DARK_GRAY, 8, (0.387 * Planet.AU, 0), 0.330e24)
    mercury.y_vel = -47.4e3

    venus: Planet = Planet("VENUS", WHITE, 14, (0.723 * Planet.AU, 0), 4.8685e24)
    venus.y_vel = -35.02e3

    planets: list[Planet] = [sun, earth, mars, mercury, venus]

    while run:

        # this is used for refreshing the background
        main_win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        for planet in planets:
            planet.update_position(planets)
            planet.draw(main_win)

        pygame.display.update()
        clock.tick(60)


main()
