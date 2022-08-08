import pygame
import constants as CONST


class UI():
    def __init__(self, screen, entities):
        self._screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.entities = entities

    @property
    def screen(self):
        return self._screen

    def set_entities(self, entities):
        self.entities = entities

    def draw(self):
        """
        Handles both single and list of entities - probably a good idea to move single into list
        """
        self.screen.fill((0, 0, 0))
        for object in self.entities:
            if isinstance(object, list):
                for item in object:
                    item.draw(self.screen)
            else:
                object.draw(self.screen)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(
            text, True, CONST.WHITE)
        self.screen.blit(text_surface, dest=(x, y))
