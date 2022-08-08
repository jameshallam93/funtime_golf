import constants as CONST


def RESISTANCE(x):
    # TODO: smoother decceleration - fix conditional branching, hard to read currently
    if x > 0:
        if x < .0005:
            return 1
        if x > 20:
            return .3
        if x > 10:
            return .185
        return .01
    if x > -.0005:
        return 1
    if x < -20:
        return .3
    if x < -10:
        return .185
    return .01


class PhysicsHandler():
    def __init__(self, ball, obstacles):
        self.ball = ball
        self.obstacles = obstacles

    def update(self):
        self.ball.velocity += self.ball.acceleration
        self.ball.velocity -= RESISTANCE(self.ball.velocity.x *
                                         self.ball.velocity.y) * self.ball.velocity
        self.ball.position += self.ball.velocity
        self.ball.acceleration *= 0
        self.collide_with_boundary()
        self.check_for_collisions()

    def collide_with_boundary(self):
        if self.ball.position.x > CONST.WINDOW_WIDTH - self.ball.radius:
            self.ball.position.x = CONST.WINDOW_WIDTH - self.ball.radius
            self.ball.velocity.x *= -1
        if self.ball.position.x < self.ball.radius:
            self.ball.position.x = self.ball.radius
            self.ball.velocity.x *= -1
        if self.ball.position.y > CONST.WINDOW_HEIGHT - self.ball.radius:
            self.ball.position.y = CONST.WINDOW_HEIGHT - self.ball.radius
            self.ball.velocity.y *= -1
        if self.ball.position.y < self.ball.radius:
            self.ball.position.y = self.ball.radius
            self.ball.velocity.y *= -1

    def check_for_collisions(self):

        ball_edges = self.ball.get_edges()
        for obstacle in self.obstacles:
            obstacle_edges = obstacle.get_edges()
            if ball_edges[0] < obstacle_edges[1] and ball_edges[1] > obstacle_edges[0] and ball_edges[2] < obstacle_edges[3] and ball_edges[3] > obstacle_edges[2]:
                # TODO: make this work for horizontal AND vertical walls.
                self.ball.velocity.x *= -1
