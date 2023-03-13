import pygame
from model.ship import *
from model.component import *
from view.game_view import *

class Game():
    __instance = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Bad Things in Outer Space, The Game")
