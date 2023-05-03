import pygame
from controller.GameController import GameController
from model.GameState import GameState
import os

class Main:
    def __init__(self):
        self.game_state = None

    def main(self):
        # Set up the game window and clock
        width = 750
        height = 750

        self.game_controller = GameController(width, height)

        self.game_controller.run_game_loop()

if __name__ == "__main__":
    Main().main()