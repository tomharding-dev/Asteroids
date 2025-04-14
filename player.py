from constants import *
from circleshape import *
from shot import *
from main import play_shoot_sound

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.score = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "dodgerblue2", self.triangle(), 0)
        
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
            
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            play_shoot_sound()
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    def add_score(self, CircleShape):
        self.score += (100 -CircleShape.radius)