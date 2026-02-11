from circleshape import CircleShape
import pygame
import random
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    #def __init__(self, x, y, radius):
        #self.x = x
        #self.y = y
        #self.radius = radius

    def draw(self, screen):
        #pygame.draw.circle(screen,"white", (self.x, self.y), self.radius, LINE_WIDTH)
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
         self.position = self.position + self.velocity*dt

    def split(self):
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


