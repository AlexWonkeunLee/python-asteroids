import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if (self.radius > ASTEROID_MIN_RADIUS):
            angle = random.uniform(20, 50)
            split1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            split2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            split1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            split2.velocity = pygame.math.Vector2.rotate(self.velocity, angle * -1) * 1.2