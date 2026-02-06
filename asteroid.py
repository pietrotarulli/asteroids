from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

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

