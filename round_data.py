import constants as CONST
import pygame

round_object_schema = {
    "x": int,
    "y": int,
    "radius": int,
    "color": (int, int, int),
    "sprite": str or None
}

wall_schema = {
    "x": int,
    "y": int,
    "width": int,
    "height": int,
    "color": (int, int, int)
}

game_info_schema = {
    "ball": round_object_schema,
    "holes": [
        round_object_schema
    ],
    "walls": [
        wall_schema
    ]
}


test_round = [{
    "ball": {
        "x": CONST.WINDOW_WIDTH / 2,
        "y": CONST.WINDOW_HEIGHT / 2,
        "radius": CONST.BALL_RADIUS,
        "color": CONST.WHITE,
        "sprite": pygame.image.load("./assets/ball1.png")
    },
    "holes": [
        {
            "x": 100,
            "y": 100,
            "radius": 30,
            "color": CONST.WHITE,
            "sprite": pygame.image.load("./assets/hole.jpg")
        }
    ],
    "walls": [
        {
            "x": 300,
            "y": 100,
            "width": 1,
            "height": 400,
            "color": CONST.WHITE
        }
    ]
}
]
