import pygame, sys, os
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import Shot
from countdown import countdown_sequence
from get_hit import game_over, lose_life

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
    pygame.display.set_caption("Asteroids")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    countdown_sequence(screen)

# ----------Main Game Loop----------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        updatable.update(dt)
        
        for a in asteroids:
            if a.collision_check(player) == True:
                if player.lives <= 1:
                    game_over(player, screen)
                    sys.exit()
                else:
                    lose_life(player, screen)
                    lives_surface = font.render(f"Lives: {player.lives}", True, "white") #not ideal
                    for a in asteroids:
                        a.kill()
                    countdown_sequence(screen, score_surface, lives_surface)
                
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
        lives_surface = font.render(f"Lives: {player.lives}", True, "white")
        screen.blit(score_surface, (20, 20))
        screen.blit(lives_surface, (20, 65))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()