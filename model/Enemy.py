import pygame
import os

from model.Spaceship import Spaceship

from model.Laser import Laser


class Enemy(Spaceship):

    def __init__(self, x, y, choice, health=100):
        super().__init__(x, y, health)

        self.COMMON_SPACE_SHIP = pygame.image.load(os.path.join("assets", "component/enemy/enemy_common.png"))
        self.UNCOMMON_SPACE_SHIP = pygame.image.load(os.path.join("assets", "component/enemy/enemy_uncommon.png"))
        self.RARE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "component/enemy/enemy_rare.png"))
        self.EPIC_SPACE_SHIP = pygame.image.load(os.path.join("assets", "component/enemy/enemy_epic.png"))
        self.LEGENDARY_SPACE_SHIP = pygame.image.load(os.path.join("assets", "component/enemy/enemy_legendary.png"))

        # Lasers
        self.COMMON_LASER = pygame.image.load(os.path.join("assets", "component/primary/projectile"
                                                                  "/projectile_primary_common.png"))
        self.UNCOMMON_LASER = pygame.image.load(os.path.join("assets", "component/primary/projectile"
                                                                  "/projectile_primary_uncommon.png"))
        self.RARE_LASER = pygame.image.load(os.path.join("assets", "component/primary/projectile"
                                                                  "/projectile_primary_rare.png"))
        self.EPIC_LASER = pygame.image.load(os.path.join("assets", "component/primary/projectile"
                                                                  "/projectile_primary_epic.png"))
        self.LEGENDARY_LASER = pygame.image.load(os.path.join("assets", "component/primary/projectile"
                                                                     "/projectile_primary_legendary.png"))
        # Laser Size
        self.SMALL_LASER = (64, 64)
        self.LARGE_LASER = (32, 256)

        self.RARITY_MAP = {
            "common": (self.COMMON_SPACE_SHIP, self.COMMON_LASER, self.SMALL_LASER),
            "uncommon": (self.UNCOMMON_SPACE_SHIP, self.UNCOMMON_LASER, self.SMALL_LASER),
            "rare": (self.RARE_SPACE_SHIP, self.RARE_LASER, self.SMALL_LASER),
            "epic": (self.EPIC_SPACE_SHIP, self.EPIC_LASER, self.LARGE_LASER),
            "legendary": (self.LEGENDARY_SPACE_SHIP, self.LEGENDARY_LASER, self.LARGE_LASER)
        }

        self.ship_img, self.laser_img, self.laser_size = self.RARITY_MAP[choice]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+8, self.y, self.laser_img, self.laser_size)
            self.lasers.append(laser)
            self.cool_down_counter = 30