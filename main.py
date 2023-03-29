import pygame
from controller.GameController import GameController
from view.GameView import GameView
from model.GameModel import GameModel
from model.GameState import GameState
from view.MenuView import Menu


class Main:
    def __init__(self):
        self.game_state = None

    def main(self):
        # Set up the game window and clock
        height = 750
        width = 750


        self.game_state = GameState(width, height)

        self.game_state.playing = True

        self.game_controller = GameController(self.game_state, None, None)

        self.menu_view = Menu(self.game_state)

        self.game_controller.run_game_loop()

if __name__ == "__main__":
    Main().main()

