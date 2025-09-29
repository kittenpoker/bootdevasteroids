import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)
    
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print ("Game over!")
                sys.exit()

        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)

        for ast in asteroids:
            for shot in shots:
                if (shot.collision(ast)):
                    ast.kill()
                    shot.kill()

        pygame.display.flip()
        t = clock.tick(60)
        dt = t/1000


if __name__ == "__main__":
    main()
