from circleshape import CircleShape
import pygame
import random
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, EXPLOSION_RADIUS, EXPLOSION_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Explosion(CircleShape):

    def draw(self, screen):
        #pygame.draw.circle(screen,"white", (self.x, self.y), self.radius, LINE_WIDTH)
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    
    def update(self, dt):
        self.position = self.position + self.velocity*dt
        print(f'position-x: {self.position.x}  position-y: {self.position.y}')
        print(f'initial position-x: {self.initial_position.x}  initial position-y: {self.initial_position.y}')
        if self.position.distance_to(self.initial_position) > 100: 
            self.kill()
            #self.explosion(1)
            #if self.position.distance_to(self.initial_position) > 50:
            #self.kill()
           # if not particle_field:
            print(f'self.initial_position: {self.initial_position}')
            #if self.initial_position == None:
            self.particle_field = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS-2)
            #particle_field.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            #
            self.particle_field.velocity = self.velocity
            self.particle_field.initial_position = self.initial_position
            #self.particle_field.kill()
            print(self.position.distance_to(self.initial_position))
        if self.position.distance_to(self.initial_position) > 200:
            print('============================================kill field=============================================')
            self.particle_field.kill()
            # if self.position.distance_to(self.initial_position) > 100:
            #self.kill()

            
    def explosion(self, n):
        for _ in range(n):
            explosion = Explosion(self.position.x, self.position.y, EXPLOSION_RADIUS)
            explosion.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED
            explosion.velocity = explosion.velocity.rotate(random.randint(-180, 180))
        print("Exploding")
