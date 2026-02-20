from circleshape import CircleShape
import pygame
import random
import weakref
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, EXPLOSION_RADIUS, EXPLOSION_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Explosion(CircleShape):

    _instances = weakref.WeakSet()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self._instances.add(self)

    @classmethod
    def get_instances(cls):
        return list(cls._instances)


    def draw(self, screen):
        #pygame.draw.circle(screen,"white", (self.x, self.y), self.radius, LINE_WIDTH)
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    
    def update(self, dt):
        self.position = self.position + self.velocity*dt
        print(f'position-x: {self.position.x}  position-y: {self.position.y}')
        print(f'initial position-x: {self.initial_position.x}  initial position-y: {self.initial_position.y}')
        if self.position.distance_to(self.initial_position) > 50 :   # Original
        #if self.position.distance_to(self.initial_position) > 100 and self.position.distance_to(self.initial_position) < 150: 
            self.kill()
           
            print(f'self.initial_position: {self.initial_position}')
            
            self.particle_field = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS-4) # Original
            self.particle_field.explosion(1)
            
            self.particle_field.velocity = self.velocity
            self.particle_field.initial_position = self.initial_position
            print(self.position.distance_to(self.initial_position))
        if self.position.distance_to(self.initial_position) > 100 : # Original
        # if self.position.distance_to(self.initial_position) > 150 and self.position.distance_to(self.initial_position) < 200:
            print('============================================kill field=============================================')
            #self.explosion_fade()
            #self.particle_field.kill() #Original
            self.particle_field.explosion(1)
            '''
            self.particle_field2 = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS)
            self.particle_field2.velocity = self.velocity
            self.particle_field2.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            self.particle_field2.velocity = self.particle_field2.velocity.rotate(random.randint(-180, 180))
            self.particle_field2.initial_position = self.initial_position
            '''
        if self.position.distance_to(self.initial_position) > 150 :
            print('============================================kill field2=============================================')
            self.explosion_fade()
            

            
    def explosion(self, n):
        for _ in range(n):
            explosion = Explosion(self.position.x, self.position.y, self.radius)
            self._instances.add(self)
            explosion.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            explosion.velocity = explosion.velocity.rotate(random.randint(-180, 180))
        print("Exploding")

    def explosion_fade(self):
        for _ in self._instances:
            _.kill()
