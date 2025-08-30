from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, PlayerRotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = PlayerRotation

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def update(self, dt):
        self.move(dt)
