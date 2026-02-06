from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    #def __init__(self, x, y, radius):
        #self.x = x
        #self.y = y
        #self.radius = radius

    def draw(self, screen):
        #pygame.draw.circle(screen,"white", (self.x, self.y), self.radius, LINE_WIDTH)
        #pygame.draw.circle(screen,"white", (self.x, self.y), SHOT_RADIUS, LINE_WIDTH)
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
         self.position = self.position + self.velocity*dt

