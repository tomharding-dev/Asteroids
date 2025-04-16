import pygame, sys, os, time
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def countdown_sequence(screen):
    countdown = 3
    
    countdown_sound_path = os.path.join('audio', 'countdown.mp3')
    countdown_sound = pygame.mixer.Sound(countdown_sound_path)
    countdown_sound.play()    
    
    while countdown > -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        if countdown == 0:
            pygame.Surface.fill(screen, "black")
            font = pygame.font.SysFont("publicpixel", 70)
            countdown_surface = font.render(f"Go!", True, "white")
            screen.blit(countdown_surface, (550,335))
            countdown -= 1
            pygame.display.flip()
            time.sleep(1)
        else:
            pygame.Surface.fill(screen, "black")
            font = pygame.font.SysFont("publicpixel", 70)
            countdown_surface = font.render(f"{countdown}", True, "white")
            screen.blit(countdown_surface, (605,335))
            pygame.display.flip()
            countdown -= 1
            time.sleep(1)

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
    screen_area = pygame.Surface.get_rect(screen)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    countdown_sequence(screen)

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
            
        font = pygame.font.SysFont("publicpixel", 30)
        score_surface = font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_surface, (20,20))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()