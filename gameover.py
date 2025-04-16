import time
import pygame
import os
from constants import *

def game_over(screen, score_surface):
    
    gameover_sound_path = os.path.join('audio', 'gameover.mp3')
    gameover_sound = pygame.mixer.Sound(gameover_sound_path)
    gameover_sound.play()
    
    timer = 0
    
    while timer < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        font = pygame.font.SysFont("publicpixel", 50)
        gameover_surface = font.render(f"Game over!", True, "red")
        screen.blit(gameover_surface, (640 - gameover_surface.get_width() // 2, 200))
        if timer % 0.5 != 0:   
            screen.blit(score_surface, (640 - score_surface.get_width() // 2, 450))
        timer += 0.25
        pygame.display.flip()
        time.sleep(0.25)