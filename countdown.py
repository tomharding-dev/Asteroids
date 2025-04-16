import pygame, time, os
from constants import *

def countdown_sequence(screen):
    countdown = 3
    
    countdown_sound_path = os.path.join('audio', 'countdown.mp3')
    countdown_sound = pygame.mixer.Sound(countdown_sound_path)
    countdown_sound.play()    
    
    while countdown > -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        font = pygame.font.SysFont("publicpixel", 70)
        if countdown == 0:
            countdown_surface = font.render(f"Go!", True, "white")
        else:
            countdown_surface = font.render(f"{countdown}", True, "white")
        screen.blit(countdown_surface, 
                    (SCREEN_WIDTH // 2 - countdown_surface.get_width() // 2, SCREEN_HEIGHT // 2 - countdown_surface.get_height() // 2)
                    )
        countdown -= 1
        pygame.display.flip()
        time.sleep(1)
