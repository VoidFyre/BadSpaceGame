class GameState:
    def __init__(self):
        self.score = 0
        self.health = 100
        self.game_over = False
        self.level_complete = False
        self.current_level = 1
        self.spaceship = None
