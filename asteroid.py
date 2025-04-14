from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=0) #unsure if need to assign this to variable
    
    def update(self, dt):
        self.position += (self.velocity * dt)