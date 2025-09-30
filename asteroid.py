import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update (self, dt):
        self.position += self.velocity * dt

    def split(self):
        rad = self.radius
        pos = self.position
        angle = random.uniform(20,50)
        vel = self.velocity
        self.kill()
        if rad <= ASTEROID_MIN_RADIUS:
            return
        new_ast_1 = Asteroid(pos.x, pos.y, rad-ASTEROID_MIN_RADIUS)
        new_ast_1.velocity = pygame.math.Vector2.rotate(vel, angle) * 1.2
        new_ast_2 = Asteroid(pos.x, pos.y, rad-ASTEROID_MIN_RADIUS)
        new_ast_2.velocity = pygame.math.Vector2.rotate(vel, -angle) * 1.2
        