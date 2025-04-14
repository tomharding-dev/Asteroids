from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2()
        
    def draw(self, screen):
        pygame.draw.circle(screen, "teal", self.position, self.radius, width=0)
    
    def update(self, dt):
        self.position += (self.velocity * dt)