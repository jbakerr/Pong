class Settings():
    """A class to create the game's settings"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (0, 0, 0)

        # Ball settings
        self.ball_width = 50
        self.ball_height = 50
        self.ball_color = (255, 255, 255)
        self.ball_speed = 20
        self.ball_direction = 1

        # Paddle settings
        self.paddle_width = 20
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = 10
