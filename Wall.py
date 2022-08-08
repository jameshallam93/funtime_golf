import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))

    def get_edges(self):
        return (self.x, self.x + self.width, self.y, self.y + self.height)
