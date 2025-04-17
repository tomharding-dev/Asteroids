import time, pygame, os, sys
from constants import *

def lose_life(player, screen):
    
    lose_life_sound_path = os.path.join('audio', 'lose_life.mp3')
    lose_life_sound = pygame.mixer.Sound(lose_life_sound_path)
    lose_life_sound.play()
    
    player.lives -= 1
    player.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    timer = 0
    
    while timer < 2.5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.Surface.fill(screen, "black")
        font = pygame.font.SysFont("publicpixel", 50)
        lifelost_surface = font.render(f"Life lost!", True, "red")
        screen.blit(lifelost_surface,
            (SCREEN_WIDTH // 2 - lifelost_surface.get_width() // 2, SCREEN_HEIGHT // 3 - lifelost_surface.get_height() // 2)
                    )
        if timer % 0.5 != 0:
            lives_remain_surface = font.render(f"Lives remaining: {player.lives}", True, "white")
            screen.blit(lives_remain_surface,
                (SCREEN_WIDTH // 2 - lives_remain_surface.get_width() // 2, (2 * SCREEN_HEIGHT // 3) - lives_remain_surface.get_height() // 2)
                        )
        timer += 0.25
        pygame.display.flip()
        time.sleep(0.25)
    
    

def game_over(player, screen):
    
    gameover_sound_path = os.path.join('audio', 'gameover.mp3')
    gameover_sound = pygame.mixer.Sound(gameover_sound_path)
    gameover_sound.play()
    
    timer = 0
    
    while timer < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.Surface.fill(screen, "black")
        font = pygame.font.SysFont("publicpixel", 50)
        gameover_surface = font.render(f"Game over!", True, "red")
        screen.blit(gameover_surface,
            (SCREEN_WIDTH // 2 - gameover_surface.get_width() // 2, SCREEN_HEIGHT // 3 - gameover_surface.get_height() // 2)
                    )
        if timer % 0.5 != 0:
            final_score_surface = font.render(f"Score: {player.score}", True, "white")
            screen.blit(final_score_surface,
                (SCREEN_WIDTH // 2 - final_score_surface.get_width() // 2, (2 * SCREEN_HEIGHT // 3) - final_score_surface.get_height() // 2)
                        )
        timer += 0.25
        pygame.display.flip()
        time.sleep(0.25)