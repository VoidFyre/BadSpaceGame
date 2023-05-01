from model.Spaceship import Spaceship
from model.Enemy import Enemy
from model.Upgrade import PowerUp
from model.GameState import GameState


class GameModel:
    def __init__(self):
        self.spaceship = Spaceship()
        self.enemies = []
        self.power_ups = []
        self.game_state = GameState()

    def update(self):
        # Update the spaceship
        self.spaceship.update()

        # Update the enemies
        for enemy in self.enemies:
            enemy.update()

        # Update the power-ups
        for power_up in self.power_ups:
            power_up.update()

        # Check for collisions between the spaceship and enemies
        for enemy in self.enemies:
            if self.spaceship.collides_with(enemy):
                self.game_state.game_over = True

        # Check for collisions between the spaceship and power-ups
        for power_up in self.power_ups:
            if self.spaceship.collides_with(power_up):
                power_up.apply_effect(self.spaceship)
                self.power_ups.remove(power_up)

        # Check if all enemies have been destroyed
        if not self.enemies:
            self.game_state.level_complete = True

        # Update the game state
        self.game_state.score = self.spaceship.score
        self.game_state.health = self.spaceship.health
