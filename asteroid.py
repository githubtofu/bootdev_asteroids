import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        r_angle = random.uniform(20, 50)
        split_1 = self.velocity.rotate(r_angle)
        split_2 = self.velocity.rotate(-r_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        print(f"NEW radius:{new_radius}")
        small_1 = Asteroid(self.position.x,
                           self.position.y, new_radius)
        small_2 = Asteroid(self.position.x,
                           self.position.y, new_radius)
        small_1.velocity = split_1 * 1.2
        small_2.velocity = split_2 * 1.2
        self.kill()
