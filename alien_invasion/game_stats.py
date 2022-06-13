class GameStats():
    """Track stats for Alien Invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start game in inactive state
        self.game_active = False
        self.score = 0
    
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit