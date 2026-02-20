
from circleshape import CircleShape
import pygame
from explosion import Explosion
import random
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, SCREEN_WIDTH, SCREEN_HEIGHT, EXPLOSION_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

        self.lives = 3
        self.respawn_delay_s = 3.0
        self.invuln_time_s = 4.0
        self.is_respawning = False
        self.respawn_timer = 0.0
        self.invuln_timer = 0.0

        # When and how to flash during invulerability period
        self.flashing_hz = 10
        self._flash_phase = 0.0

        self.exploding = False

        self.acceleration = 0      # thrust strength
        self.max_speed = 500
        self.drag = 0.95             # space friction

        

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        '''
        if self._flash_phase > 0 :
            self.flashing_hz -= 1
            if  self.flashing_hz % 4 == 0:
                self.velocity = pygame.Vector2(0, 0)
                return
        '''
        flashing = (self.invuln_timer > 0) #or self.is_respawning

        if flashing:
            self.exploding =False
            self.velocity = pygame.Vector2(0, 0)
         # Toggle visibility at flash_hz
            period = 1.0 / self.flashing_hz
            if int(self._flash_phase / period) % 2 == 0:
                return  # skip drawing this frame
        
        if not self.exploding:
            pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        

    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def update(self, dt):
        # When and how to flash during invulerability period
        '''
        self._flash_phase = self.invuln_timer
        if self.invuln_timer > 0 and self._flash_phase > 0:
            self._flash_phase -= dt
        '''
        if self.invuln_timer > 0 or self.is_respawning:
            self._flash_phase += dt
        else:
            self._flash_phase = 0.0

        self.shot_cooldown_timer -= dt
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

        #Keep initial momentum
        self.position += self.velocity * dt
        # Wrap around the screen
        self.wrap()
        
    
    def move(self, dt):
        
        unit_vector = pygame.Vector2(0, 1)
        forward = unit_vector.rotate(self.rotation)
        #forward = unit_vector
        
        # Apply thrust (acceleration)
        self.acceleration += 2
        self.velocity += forward * self.acceleration * dt

        # Clamp max speed
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Apply drag
        self.velocity *= self.drag
        
        # Move
        self.position += self.velocity * dt

        # Wrap around the screen
        #self.wrap()


    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        # shot1 = Shot(self.x, self.y, SHOT_RADIUS)
        shot1 = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot1.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED

    def respawn_player(self, screen):
        print("Respawning")
        #pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        #pygame.draw.polygon(screen, "black", self.triangle(), LINE_WIDTH)
        self.position.x = SCREEN_WIDTH / 2
        self.position.y = SCREEN_HEIGHT / 2
        #pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        self.draw(screen)

    def wrap(self):
        # Wrap around the screen
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        
    def explosion(self, n):
        #self.kill()
        self.exploding = True
        for _ in range(n):
            explosion = Explosion(self.position.x, self.position.y, 1)
            #self._instances.add(self)
            explosion.velocity = pygame.Vector2(1, 0)*EXPLOSION_SPEED #+ self.velocity
            #explosion.velocity = self.velocity
            explosion.velocity = explosion.velocity.rotate(random.randint(-180, 180))
            #explosion.velocity = explosion.velocity.rotate(self.rotation)
        print("Exploding")