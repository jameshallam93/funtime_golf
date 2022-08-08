import pygame


class Menu():
    def __init__(self, UI):
        self.UI = UI

    def run(self):
        while True:
            self.UI.draw()
            pygame.display.flip()
            pygame.display.update()
