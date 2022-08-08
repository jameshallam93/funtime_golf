import pygame
import constants as CONST


class Ball(pygame.sprite.Sprite):
    def __init__(self,  x, y, radius, sprite):
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.sprite = sprite
        self.rect = sprite.get_rect()
        self.acceleration = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)

    def draw(self, screen):
        screen.blit(self.sprite, (self.position.x, self.position.y))

    def draw_line(self, screen, x, y):
        pygame.draw.line(screen, (255, 255, 255), self.get_centre(), (x, y), 3)

    def move(self, x, y):
        self.position.x = x
        self.position.y = y

    def get_pos(self):
        return self.position.x, self.position.y

    def get_centre(self):
        return self.position.x + (self.radius/2), self.position.y + (self.radius/2)

    def set_in_motion(self, x, y):
        print("setting in motion")
        print(x, y)
        if x > CONST.MAX_FORCE:
            x = CONST.MAX_FORCE
        if x < -CONST.MAX_FORCE:
            x = -CONST.MAX_FORCE
        if y > CONST.MAX_FORCE:
            y = CONST.MAX_FORCE
        if y < -CONST.MAX_FORCE:
            y = -CONST.MAX_FORCE
        self.acceleration = pygame.math.Vector2(x, y)

    def stop(self):
        self.velocity.x = 0
        self.velocity.y = 0

    def get_edges(self):
        return (self.position.x, self.position.x + self.radius, self.position.y, self.position.y + self.radius)
