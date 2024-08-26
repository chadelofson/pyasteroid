from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    # Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)




    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in player.bullets:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()


        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



        elapsed = clock.tick(60)
        dt = elapsed / 1000


if __name__ == "__main__":
    main()
