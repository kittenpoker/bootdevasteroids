import pygame
from circleshape import *
from constants import *
#print(constants.PLAYER_RADIUS)


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius /1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta):
        self.rotation = (self.rotation + delta) % 360
    
    def move(self, dt, thrust_dir):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.velocity += forward * (THRUST *thrust_dir) * dt
        self.position += self.velocity * dt
        if thrust_dir == 0:
            self.velocity *= max(0.0, 1.0 - DAMPING * dt)
        self.position.x = max(self.radius, min(self.position.x, SCREEN_WIDTH - self.radius))
        self.position.y = max(self.radius, min(self.position.y, SCREEN_HEIGHT - self.radius))
        