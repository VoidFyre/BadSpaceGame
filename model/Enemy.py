import pygame
import os

from model.Spaceship import Spaceship

from model.Laser import Laser


class Enemy(Spaceship):

    def __init__(self, x, y, rarity, wave):
        super().__init__(x, y, health = 20, ship_img = None)
        self.rarity = rarity

        # Create a timer for enemy shooting
        self.enemy_shoot_timer = pygame.time.get_ticks()

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
        self.LARGE_LASER = (28, 100)

        # Health
        self.COMMON_HEALTH = 100 * (1 + (0.1 * wave))
        self.UNCOMMON_HEALTH = 150 * (1 + (0.1 * wave))
        self.RARE_HEALTH = 200 * (1 + (0.1 * wave))
        self.EPIC_HEALTH = 250 * (1 + (0.1 * wave))
        self.LEGENDARY_HEALTH = 400 * (1 + (0.1 * wave))

        # Damage
        self.COMMON_DMG = 10
        self.UNCOMMON_DMG = 15
        self.RARE_DMG = 20
        self.EPIC_DMG = 25
        self.LEGENDARY_DMG = 40

        self.RARITY_MAP = {
            "common": (self.COMMON_SPACE_SHIP, self.COMMON_LASER, self.SMALL_LASER, self.COMMON_HEALTH, self.COMMON_DMG),
            "uncommon": (self.UNCOMMON_SPACE_SHIP, self.UNCOMMON_LASER, self.SMALL_LASER, self.UNCOMMON_HEALTH, self.UNCOMMON_DMG),
            "rare": (self.RARE_SPACE_SHIP, self.RARE_LASER, self.SMALL_LASER, self.RARE_HEALTH, self.RARE_DMG),
            "epic": (self.EPIC_SPACE_SHIP, self.EPIC_LASER, self.LARGE_LASER, self.EPIC_HEALTH, self.EPIC_DMG),
            "legendary": (self.LEGENDARY_SPACE_SHIP, self.LEGENDARY_LASER, self.LARGE_LASER, self.LEGENDARY_HEALTH, self.LEGENDARY_DMG)
        }

        self.ship_img, self.laser_img, self.laser_size, self.health, self.laser_dmg = self.RARITY_MAP[self.rarity]
        self.mask = pygame.mask.from_surface(self.ship_img)


    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+8, self.y, self.laser_img, self.laser_size)
            self.lasers.append(laser)
            self.cool_down_counter = 30

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_height(self):
        return self.ship_img.get_height()

    def get_width(self):
        return self.ship_img.get_width()