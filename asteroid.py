import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray40", self.position, self.radius, width=0)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        
        velocity1 = (self.position.rotate(angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity2 = (self.position.rotate(-angle))
        
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = velocity1 * 0.5
        
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = velocity2 * 0.5