class GameStats():
    """A class to track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        # self.reset_stats()

        # Start Alien Invasion if in active state
        self.game_active = False

    # def reset_stats(self):
    #     """Initialize the statistics that can change during the game"""
    #     self.ships_left = self.ai_settings.ship_limit
    #     self.score = 0
