import pygame, sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,
                             SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = {shots, updatable, drawable}
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    #player is a triangle
    my_player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    my_clock = pygame.time.Clock()
    my_field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill((0,0,0))
        for an_entity in updatable:
            an_entity.update(dt)
        for an_asteroid in asteroids:
            if an_asteroid.collide(my_player):
                print("Game over!")
                sys.exit()
            for a_shot in shots:
                if an_asteroid.collide(a_shot):
                    an_asteroid.split()
                    a_shot.kill()
        for an_entity in drawable:
            an_entity.draw(screen)
        pygame.display.flip()
        dt = my_clock.tick(60) / 1000 #mili to sec

if __name__ == "__main__":
    main()

