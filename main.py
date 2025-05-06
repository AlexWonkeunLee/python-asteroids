# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots)
    field = AsteroidField()
    while(1 > 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        shots.update(dt)
        for shot in shots:
            shot.draw(screen)
            for asteroid in asteroids:
                if (asteroid.isCollision(shot)):
                    asteroid.split()
                    shot.kill()
        for asteroid in asteroids:
            if (asteroid.isCollision(player)):
                print("Game over!")
                sys.exit(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        

if __name__ == "__main__":
    main()