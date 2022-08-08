import pygame


class Hole(pygame.sprite.Sprite):
    def __init__(self,  x, y, radius, sprite):
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.sprite = sprite
        self.rect = sprite.get_rect()

    def draw(self, screen):
        screen.blit(self.sprite, (self.position.x, self.position.y))

    def get_pos(self):
        return self.position.x, self.position.y

    def get_centre(self):
        return self.position.x + (self.radius/2), self.position.y + (self.radius/2)

    def get_edges(self):
        return (self.position.x, self.position.x + self.radius, self.position.y, self.position.y + self.radius)

    def contains_ball(self, ball):
        if ball.get_centre()[0] > self.position.x and ball.get_centre()[0] < self.position.x + self.radius and ball.get_centre()[1] > self.position.y and ball.get_centre()[1] < self.position.y + self.radius:
            ball.move(self.position.x - 30, self.position.y - 20)
            return True
        return False
