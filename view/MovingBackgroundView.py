import pygame
import os
import math


class MovingBackgroundView:

    WINDOW_SIZE = (750, 750)
    FPS = 60

    def __init__(self):

        self.game_state = None

        # Load background images
        self.background_image = pygame.image.load(os.path.join("assets", "space_background_9.png")).convert_alpha()

        self.bg_height = self.background_image.get_height()
        self.bg_rect = self.background_image.get_rect()

        self.background_image = pygame.transform.scale(self.background_image, (self.WINDOW_SIZE[0], self.WINDOW_SIZE[1]))

        # define game variables
        self.scroll = 0

    def set_game_state(self, game_state):
        self.game_state = game_state

    def run(self):

        self.scroll -= 1

        if abs(self.scroll) > self.game_state.DISPLAY_H:
            self.scroll = 0

        # draw scrolling background
        for i in range(0, 5):
            self.game_state.window.blit(self.background_image, (0, i * self.game_state.DISPLAY_H + self.scroll))
            self.bg_rect.y = i * self.game_state.DISPLAY_H + self.scroll

