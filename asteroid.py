from circleshape import CircleShape
import pygame
import random
from explosion import Explosion
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, EXPLOSION_RADIUS, EXPLOSION_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

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
        #self.explode()
        #self.kill()
        
        explosion = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS)
        explosion.kill()
        explosion.explosion(10)
        self.kill()
        #print(explosion)
        #print(f'In split method: self.position.x:{self.position.x}  self.position.y:{self.position.y}')
        #explosion.explosion(self.position)
        
        #Explosion.explosion(self.position)
        #self.explosion(self.position)

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
    
    #def explode(self):
        #explosion.explosion(self.position.x, self.position.y)
        '''
        for _ in range(10):
            explosion = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS)
            explosion.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            explosion.velocity = explosion.velocity.rotate(random.randint(-180, 180))
        print("Exploding")
        '''

    '''
    def explosion(self, position):
    #def spawn(self, radius, position, velocity):
        for _ in range(10):
            shrapnel = Asteroid(position.x, position.y, EXPLOSION_RADIUS)
            shrapnel.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            shrapnel.velocity = shrapnel.velocity.rotate(random.randint(-180, 180))
        #position = edge[1](random.uniform(0, 1))
        #kind = random.randint(1, ASTEROID_KINDS)
        #self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
    '''

    '''
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)
        self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
        '''