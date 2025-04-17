import pygame, time, os, sys
from constants import *

def countdown_sequence(screen, score_surface = None, lives_surface = None):
    countdown = 3
    
    countdown_sound_path = os.path.join('audio', 'countdown.mp3')
    countdown_sound = pygame.mixer.Sound(countdown_sound_path)
    countdown_sound.play()    
    
    while countdown > -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.Surface.fill(screen, "black")
        font = pygame.font.SysFont("publicpixel", 70)
        if countdown == 0:
            countdown_surface = font.render(f"Go!", True, "white")
        else:
            countdown_surface = font.render(f"{countdown}", True, "white")
        screen.blit(countdown_surface, 
            (SCREEN_WIDTH // 2 - countdown_surface.get_width() // 2, SCREEN_HEIGHT // 2 - countdown_surface.get_height() // 2)
                    )
        if score_surface != None:
            screen.blit(score_surface, (20, 20))
        if lives_surface != None:
            screen.blit(lives_surface, (20, 65))
            
        countdown -= 1
        pygame.display.flip()
        time.sleep(1)
