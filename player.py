import pygame
from circleshape import *
from constants import *

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

    def update(self, dt):
        pressed = pygame.key.get_pressed()
        
        turn_direction = 0
        if pressed[pygame.K_LEFT]:
            turn_direction -= 1
        if pressed[pygame.K_RIGHT]:
            turn_direction += 1
        
        thrust_dir = 0
        if pressed[pygame.K_UP]:
            thrust_dir += 1
        if pressed[pygame.K_DOWN]:
            thrust_dir -= 1

        self.rotate(TURN_RATE * dt * turn_direction)
        self.move(dt, thrust_dir)


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
        