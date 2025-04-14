import pygame, sys, os
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def play_shoot_sound():
    shoot_sound_path = os.path.join('audio', 'shoot.mp3')
    shoot_sound = pygame.mixer.Sound(shoot_sound_path)
    shoot_sound.play()

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    
    font = pygame.font.SysFont("publicpixel", 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for a in asteroids:
            if a.collision_check(player) == True:
                print(f"Game over! Your score was: {player.score}!")
                sys.exit()
                
        for a in asteroids:
            for s in shots:
                if a.collision_check(s) == True:
                    a.split()
                    s.kill()
                    player.add_score(a)
        
        pygame.Surface.fill(screen, "black")
        
        for d in drawable:
            d.draw(screen)
            
        score_surface = font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_surface, (20,20))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()