import pygame
from Physics import PhysicsHandler
import constants as CONST


class Round():
    def __init__(self, UI, ball, obstacles, hole):
        self.UI = UI
        self.ball = ball
        self.obstacles = obstacles
        self.holes = hole
        # currently, have to feed entities in in the order you want them to be rendered - should fix this.
        self._entities = [self.obstacles, self.holes, self.ball]
        self.shot_count = 0
        self.shot_limit = 10
        self.physics = PhysicsHandler(
            self.ball, self.obstacles)

    @property
    def entities(self):
        return self._entities

    def get_score_string(self):
        return "Hole in 1!" if self.shot_count == 1 else "You got it in {} shots!".format(self.shot_count)

    def handle_win(self):
        pygame.display.flip()
        pygame.display.update()
        self.ball.stop()
        text = self.get_score_string()
        self.UI.draw_text(text, 100, 100)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.ball.move(CONST.WINDOW_WIDTH/2, CONST.WINDOW_HEIGHT/2)
        self.ball.stop()
        # TODO: return to main menu (also, make main menu)

    def handle_loss(self):
        pygame.display.flip()
        pygame.display.update()
        self.ball.stop()
        text = "You lose!"
        self.UI.draw_text(text, 100, 100)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.ball.move(CONST.WINDOW_WIDTH/2, CONST.WINDOW_HEIGHT/2)
        self.ball.stop()
        # TODO: decide what to do here

    def run(self):
        self.UI.set_entities(self.entities)
        self.shot_count = 0

        while True:
            self.physics.update()

            self.UI.draw()

            mouse_loc = pygame.mouse.get_pos()
            ball_loc = self.ball.get_centre()

            # TODO: Move this to UI - it has access to the ball, just need to find a nice way of grabbing it
            if self.ball.velocity == (0, 0):
                self.ball.draw_line(
                    self.UI.screen, mouse_loc[0], mouse_loc[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # reset ball - for testing
                    if event.key == pygame.K_LCTRL:
                        self.ball.move(400, 300)

                if self.ball.velocity == (0, 0):
                    if event.type == pygame.MOUSEBUTTONUP:
                        # shot time baby
                        self.ball.set_in_motion(((ball_loc[0] - mouse_loc[0]) / 40),
                                                ((ball_loc[1] - mouse_loc[1]) / 40))
                        self.shot_count += 1

            pygame.display.flip()
            pygame.display.update()
            # eventually check all holes (if multiple in the round)
            if self.holes[0].contains_ball(self.ball):
                self.handle_win()
            if self.shot_count > self.shot_limit:
                self.handle_loss()
