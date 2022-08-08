import pygame
from Round import Round
import constants as CONST
from Ball import Ball
from Hole import Hole
from Wall import Wall
from UI import UI as GUI
from round_data import test_round


pygame.display.set_caption("James' cooltime game")

pygame.display.set_icon(CONST.ICON)


class Game:
    def __init__(self, round_data):
        pygame.init()
        pygame.get_init()
        self.screen = pygame.display.set_mode(
            (CONST.WINDOW_WIDTH, CONST.WINDOW_HEIGHT))

        self.UI = GUI(self.screen, entities=[])
        self.rounds = [self.create_round(round_datum, self.UI)
                       for round_datum in round_data]

    def create_round(self, round_data, UI):
        print(round_data)
        ball_data = round_data["ball"]
        holes_data = round_data["holes"]
        walls_data = round_data["walls"]

        ball = Ball(ball_data["x"], ball_data["y"],
                    ball_data["radius"],  ball_data["sprite"])
        holes = [Hole(hole_data["x"], hole_data["y"], hole_data["radius"],
                      hole_data["sprite"]) for hole_data in holes_data]
        walls = [Wall(wall_data["x"], wall_data["y"], wall_data["width"],
                      wall_data["height"], wall_data["color"]) for wall_data in walls_data]

        return Round(UI, ball, walls, holes)

    def run(self):
        # TODO: add menu and way of selecting rounds
        for round in self.rounds:
            round.run()


if __name__ == "__main__":
    game = Game(round_data=test_round)
    game.run()
