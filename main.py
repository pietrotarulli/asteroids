from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from explosion import Explosion
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    font = pygame.font.Font(None, 36)
    score = 0
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explode = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (explode, updatable, drawable)

    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    print(asteroidfield)
    print(explode)
    print(shots)
    

    while True:
        log_state()
        #for event in pygame.event.get():
        #    pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        score_surf = font.render(f"Score:{score}", True, "white")
        screen.blit(score_surf, (10, 10))
        score_surf = font.render(f"Lives:{player1.lives}", True, "white")
        screen.blit(score_surf, (400, 10))
        #asteroidfield.spawn()
        updatable.update(dt)
        
        if player1.invuln_timer > 0:
            player1.invuln_timer -= dt
        if player1.is_respawning:
            player1.respawn_timer -= dt    
            if player1.respawn_timer <= 0:
                player1.respawn_player(screen)
                player1.is_respawning = False
                player1.invuln_timer = player1.invuln_time_s

        #print(f"{player1.invuln_timer} {player1.is_respawning}")
        if player1.invuln_timer <= 0 and not player1.is_respawning:
            for asteroid in asteroids:
                if asteroid.collides_with(player1):
                    log_event("player_hit")
                    #print("player_hit")
                    player1.lives -= 1
                    log_event("player_hit")
                    #print(f"Player Lives {player1.lives}")

                    if player1.lives < 0:
                        print("Game Over!")
                        sys.exit()
                    #player1.kill()
                    player1.is_respawning = True
                    player1.respawn_timer = player1.respawn_delay_s
                    break
                    #player1.kill()
                    #time.sleep(5)
                    #player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    #print("Game over!")
                    #sys.exit()
        
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        #asteroid.kill()
                        asteroid.split()
                        #asteroid.explode()
                        '''
                        print(shots)
                        print(explode)
                        for bits in explode:
                            print(bits)
                            bits.explosion()
                        '''
                        shot.kill()
                        #if asteroid.radius == ASTEROID_MIN_RADIUS:
                        #    score += 200
                        #elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        #    score += 50
                        score += {ASTEROID_MIN_RADIUS:200, 40: 100, ASTEROID_MAX_RADIUS:50}[asteroid.radius]
                                  

        for object in drawable:
            object.draw(screen)
            #player1.update(dt)
            #player1.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        # print(dt)


if __name__ == "__main__":
    main()



"""
Extending the Project
You've done all the required steps, but if you'd like to make the game your own, here are some ideas:

Add a scoring system
Implement multiple lives and respawning
Add an explosion effect for the asteroids
Add acceleration to the player movement
Make the objects wrap around the screen instead of disappearing
Add a background image
Create different weapon types
Make the asteroids lumpy instead of perfectly round
Make the ship have a triangular hit box instead of a circular one
Add a shield power-up
Add a speed power-up
Add bombs that can be dropped
"""