import pygame
from controller.GameController import GameController
from model.GameState import GameState

class Main:
    def __init__(self):
        self.game_state = None

    def main(self):
        # Set up the game window and clock
        height = 750
        width = 750

        self.game_state = GameState(width, height)

        self.game_controller = GameController(self.game_state, None, None)

        self.game_controller.run_game_loop()

if __name__ == "__main__":
    Main().main()

