from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        RightAngle = self.velocity.rotate(angle)
        LeftAngle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_R = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_L = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_R.velocity = RightAngle * 1.2
        new_asteroid_L.velocity = LeftAngle * 1.2
