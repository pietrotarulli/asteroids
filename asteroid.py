from circleshape import CircleShape
import pygame
import random
from explosion import Explosion
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, EXPLOSION_RADIUS, EXPLOSION_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
         self.position = self.position + self.velocity*dt
         # Wrap around the screen
         if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
         if self.position.x < 0:
             self.position.x = SCREEN_WIDTH
        
         if self.position.y > SCREEN_HEIGHT:
             self.position.y = 0
         if self.position.y < 0:
             self.position.y = SCREEN_HEIGHT

    def split(self): 
        explosion = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS)
        explosion.kill()
        explosion.explosion(10)
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.randint(20, 50)
            asteroid1_angle = self.velocity.rotate(angle)
            asteroid2_angle = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_angle*1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = asteroid2_angle*1.2
    
    