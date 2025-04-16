import pygame, time, os

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
