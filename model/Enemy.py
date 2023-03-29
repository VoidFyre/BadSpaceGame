import pygame
import os

from model.Spaceship import Spaceship

from model.Laser import Laser


class Enemy(Spaceship):

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)

        self.RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        self.GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
        self.BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

        # Lasers
        self.RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        self.GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        self.BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        self.YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

        self.COLOR_MAP = {
            "red": (self.RED_SPACE_SHIP, self.RED_LASER),
            "green": (self.GREEN_SPACE_SHIP, self.GREEN_LASER),
            "blue": (self.BLUE_SPACE_SHIP, self.BLUE_LASER)
        }

        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1